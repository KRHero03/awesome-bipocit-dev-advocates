# {{site.title}}

This is an awesome list of BIPOC Developer Advocates

----
{% for advocate, adv_data in advocates %}
### [{{advocate}}]({{adv_data.website}}) - {{adv_data.company}}
{% if adv_data.github %}[![github](assets/github-square-brands.png)](https://github.com/{{adv_data.github}}){% endif %}{% if adv_data.twitter %}[![twitter](assets/twitter-square-brands.png)](https://twitter.com/{{adv_data.twitter}}){% endif %}{% if adv_data.youtube %}[![youtube](assets/youtube-brands.png)]({{adv_data.youtube}}){% endif %}{% if adv_data.linkedIn %}[![linkedIn](assets/linkedin-brands.png)](https://linkedin.com/in/{{adv_data.linkedIn}}){% endif %}{% if adv_data.twitch %}[![twitch](assets/twitch-brands.png)](https://twitch.com/in/{{adv_data.twitch}}){% endif %}

{% endfor %}
----

{% include "whats-this.md" %}
{% include "whats-the-plan.md" %}
{% include "missing.md" %}
