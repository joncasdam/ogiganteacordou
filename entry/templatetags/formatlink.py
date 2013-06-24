import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def format(link):
    #  Format youtube urls to embed link
    if ( re.match(r'http(s)*://www.youtube.com/embed/(.*)', link, re.I) is None ):
    	pattern = r'(http(s)*://youtu.be/(?P<v1>.*))|(http(s)*://(www.)*youtube.com(.*)v=(?P<v2>.*)(&)*$)'

    	m = re.match(pattern, link, re.I)
    	if (m is not None):
    		video = m.group('v1') or m.group('v2')
    		return 'http://www.youtube.com/embed/' + video
    else:
		return link