class Matcher:
    def or_name(self, node):
        if 'name' in node.annotations:
            return PrefixMatcher(node.annotations['name'])
        else:
            return self

class EmptyMatcher(Matcher):
    def match(self, node):
        return False

class PrefixMatcher(Matcher):
    def __init__(self, prefix):
        self._prefix = prefix

    def match(self, node):
        return (
            'path' in node.attrs and 
            node.attrs['path'][0] == self._prefix
        )

class UnionMatcher(Matcher):
    def __init__(self, matchers):
        self._matchers = matchers

    def match(self, node):
        for matcher in self._matchers:
            if (matcher.match(node)):
                return True
        return False
