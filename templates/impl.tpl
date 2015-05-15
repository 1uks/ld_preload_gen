{{func.return_type}} {{func.name}}({{func|joinargs|trim}})
{
    {% if func.return_type != "void" %}return {% endif %}orig_{{func.name}}({{func.args|join(", ", attribute="name")}});
}
