#!/usr/bin/env python2

import argparse
import tempfile
import os
import logging
import jinja2
from constants import DEFAULT_HEADERS, INCLUDE_PATHS
from pygccxml import parser
from pygccxml.declarations import matcher
from pygccxml.utils import loggers
loggers.cxx_parser.setLevel(logging.ERROR)


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Parser(object):
    def __init__(self, filename):
        self.filename = filename
        self.ns = parser.parse([filename], parser.gccxml_configuration_t())[0]

    def _remove_ns(self, string):
        return string.strip().lstrip("::")

    def _prettify(self, string):
        return string.strip().lstrip("__")

    def _no_restrict(self, string):
        return string.replace("__restrict__", "")

    def _prettify_type(self, string):
        return self._prettify(self._remove_ns(self._no_restrict(string)))

    def _is_struct(self, type):
        while hasattr(type, "base"):
            type = type.base
        if hasattr(type, "declaration"):
            if hasattr(type.declaration, "class_type"):
                if type.declaration.class_type == "struct":
                    return True
        return False

    def yield_functions(self, func_names):
        for func_name in func_names:
            try:
                func = self.ns.free_function(func_name)
            except matcher.declaration_not_found_t:
                continue
            if not func.required_args:
                args = [{"name": "", "type": "void"}]
            else:
                args = []
                for arg in func.required_args:
                    type = self._prettify_type(arg.type.decl_string)
                    if self._is_struct(arg.type):
                        type = "struct " + type
                    args.append({
                        "name": self._prettify(arg.name),
                        "type": type,
                    })
            header = func.location.file_name
            for path in INCLUDE_PATHS:  # refactor
                if func.location.file_name.startswith(path):
                    header = header.rsplit(path)[1]
                    break
            return_type = self._remove_ns(func.return_type.decl_string)
            if self._is_struct(func.return_type):
                return_type = "struct " + return_type
            yield {
                "name": self._remove_ns(func.name),
                "return_type": return_type,
                "header": header,
                "args": args,
            }


class CodeGenerator(object):
    def __init__(self):
        self.functions = []

    def add_function(self, function):
        self.functions.append(function)

    def generate(self):
        raise NotImplementedError


class CCodeGenerator(CodeGenerator):
    def __init__(self):
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, "templates")),
            trim_blocks=True,
        )
        self.env.filters["joinargs"] = self._joinargs
        super(CCodeGenerator, self).__init__()

    def _joinargs(self, func):
        return ", ".join(" ".join(arg.values()) for arg in func["args"])

    def generate(self):
        typedef_tpl = self.env.get_template("typedef.tpl")
        typedefs = []
        impl_tpl = self.env.get_template("impl.tpl")
        impl_variadic_tpl = self.env.get_template("impl_variadic.tpl")
        impls = []
        include_tpl = self.env.get_template("include.tpl")
        includes = []
        orig_cache_tpl = self.env.get_template("orig_cache.tpl")
        orig_caches = []
        has_variadic = False
        for func in self.functions:
            typedef = typedef_tpl.render(func=func)
            typedefs.append(typedef)
            if func["args"][-1]["type"] == "...":  # variadic
                impl = impl_variadic_tpl.render(func=func)
                has_variadic = True
            else:
                orig_cache = orig_cache_tpl.render(func=func)
                orig_caches.append(orig_cache)
                impl = impl_tpl.render(func=func)
            impls.append(impl)
            include = include_tpl.render(func=func)
            if include not in includes:
                includes.append(include)
        return self.env.get_template("source.tpl").render(
            includes=includes, typedefs=typedefs, orig_caches=orig_caches, impls=impls, has_variadic=has_variadic
        )


class RustCodeGenerator(CodeGenerator):
    pass


def main(headers, funcs):
    fd, tmpfile = tempfile.mkstemp(suffix=".h")
    with os.fdopen(fd, "w") as fileobj:
        fileobj.write("\n".join("#include <%s>" % header for header in headers))
    try:
        parser = Parser(tmpfile)
    finally:
        os.unlink(tmpfile)
    generator = CCodeGenerator()
    for func in parser.yield_functions(funcs):
        generator.add_function(func)
    print generator.generate()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-H", "--header", nargs="*", dest="headers",
        default=DEFAULT_HEADERS)
    argparser.add_argument("func", nargs="+")
    args = argparser.parse_args()
    main(args.headers, args.func)
