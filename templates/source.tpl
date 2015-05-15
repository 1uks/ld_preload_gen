#define _GNU_SOURCE
#include <dlfcn.h>
{% if has_variadic %}
#include <stdarg.h>
{% endif %}
{{ includes|join("\n") }}

{{ typedefs|join("\n") }}

{{ orig_caches|join("\n") }}

{{ impls|join("\n\n") }}
