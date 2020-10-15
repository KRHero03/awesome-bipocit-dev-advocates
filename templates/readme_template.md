# {site.title}

{% include "whats-this.md" %}

----
{% for advocate, adv_data in advocates %}
### [{{advocate}}]({{adv_data.website}}) - {{adv_data.company}}
{% endfor %}
----

{% include "whats-the-plan.md" %}

{% include "missing.md" %}
