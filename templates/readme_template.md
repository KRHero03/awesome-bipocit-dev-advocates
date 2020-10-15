# {{site.title}}

This is an awesome list of BIPOC Developer Advocates

----
{% for advocate, adv_data in advocates %}
### [{{advocate}}]({{adv_data.website}}) - {{adv_data.company}}
{% if adv_data.github %}[![github](.assets/github-square-brands.svg)]({{adv_data.github}}){% endif %}
{% endfor %}
----

{% include "whats-this.md" %}
{% include "whats-the-plan.md" %}
{% include "missing.md" %}
