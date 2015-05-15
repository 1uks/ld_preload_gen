{{func.return_type}} {{func.name}}({{func|joinargs|trim}})
{
    va_list args;
    va_start(args, {{func.args[-2].name}});

{% if func.return_type != "void" %}
    {{func.return_type}} ret = v{{func.name}}({{func.args[:-1]|join(", ", attribute="name")}}, args);
{% else %}
    v{{func.name}}({{func.args[:-1]|join(", ", attribute="name")}}, args);
{% endif %}

    va_end(args);
{% if func.return_type != "void" %}

    return ret;
{% endif %}
}
