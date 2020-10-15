# {site.title}

{% include "whats-this.md" %}

----
{% for advocate in advocates %}

### [{{advocate.name}}]({{advocate.url}}) - {{advocate.company}}

{% for link in advocates.links %}
- [link.title](link.name)
{% endfor %}

{% endfor %}
----

{% include "whats-the-plan.md" %}

{% include "missing.md" %}
