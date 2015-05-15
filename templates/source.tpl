#define _GNU_SOURCE
#include <dlfcn.h>
{% if has_variadic %}
#include <stdarg.h>
{% endif %}
{{ includes|join("\n") }}

{{ typedefs|join("\n") }}
{% if orig_caches %}

{{ orig_caches|join("\n\n") }}
{% endif %}

{{ impls|join("\n\n") }}
