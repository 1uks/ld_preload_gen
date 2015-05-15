{{func.return_type}} {{func.name}}({{func|joinargs|trim}})
{
    va_list args;
    va_start(args, {{func.args[-2].name}});

    {{func.return_type}} ret = v{{func.name}}({{func.args[:-1]|join(", ", attribute="name")}}, args);

    va_end(args);

    return ret;
}
