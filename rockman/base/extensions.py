from django import template as django_template
from jinja2 import nodes, contextfunction, ext


# The actual Django templatag for Jinja
class Django(ext.Extension):
    tags = set(['django'])

    def preprocess(self, source, name, filename=None):
        source = source.replace('{% django %}', '{% django %}{% raw %}')
        source = source.replace('{% enddjango %}',
            '{% endraw %}{% enddjango %}')
        return source

    def parse(self, parser):
        lineno = parser.stream.next().lineno

        while not parser.stream.next().test('block_end'):
            pass

        body = nodes.Const(parser.stream.next().value)

        while not parser.stream.current.test('block_end'):
            parser.stream.next()

        return nodes.Output([
            self.call_method('_django', args=[body], kwargs=[]),
        ]).set_lineno(lineno=lineno)

    @contextfunction
    def _django(self, context, html):
        context = django_template.RequestContext(context['request'], context)
        return django_template.Template(html).render(context)
