# {{site.title}}

This is an awesome list of BIPOC Developer Advocates

----
{% for advocate, adv_data in advocates %}
### [{{advocate}}]({{adv_data.website}}) - {{adv_data.company}}
{% endfor %}
----

{% include "whats-the-plan.md" %}
{% include "missing.md" %}
{% include "whats-this.md" %}
