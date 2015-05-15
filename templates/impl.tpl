{{func.return_type}} {{func.name}}({{func|joinargs|trim}})
{
    orig_{{func.name}}_f_type orig_{{func.name}} = (orig_{{func.name}}_f_type) dlsym(RTLD_NEXT, "{{func.name}}");

    {% if func.return_type != "void" %}return {% endif %}orig_{{func.name}}({{func.args|join(", ", attribute="name")}});
}
