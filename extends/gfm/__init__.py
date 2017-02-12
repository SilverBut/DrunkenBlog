# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from extends.gfm import autolink
from extends.gfm import automail
from extends.gfm import hidden_hilite
from extends.gfm import semi_sane_lists
from extends.gfm import spaced_link
from extends.gfm import strikethrough

from markdown.extensions import Extension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.smart_strong import SmartEmphasisExtension
from markdown.extensions.tables import TableExtension

#from extends import gfm
from markdown.extensions.nl2br import Nl2BrExtension


AutolinkExtension = autolink.AutolinkExtension
AutomailExtension = automail.AutomailExtension
HiddenHiliteExtension = hidden_hilite.HiddenHiliteExtension
SemiSaneListExtension = semi_sane_lists.SemiSaneListExtension
SpacedLinkExtension = spaced_link.SpacedLinkExtension
StrikethroughExtension = strikethrough.StrikethroughExtension

def makeExtension(*args, **kwargs):
    return GithubFlavoredMarkdownExtension(*args, **kwargs)


class PartialGithubFlavoredMarkdownExtension(Extension):
    """An extension that's as compatible as possible with GFM.
    This extension aims to be compatible with the variant of GFM that GitHub
    uses for Markdown-formatted gists and files (including READMEs). This
    variant seems to have all the extensions described in the `GFM
    documentation`_, except:
    - Newlines in paragraphs are not transformed into ``br`` tags.
    - Intra-Github links to commits, repositories, and issues are not supported.
    .. _the GFM documentation: http://github.github.com/github-flavored-markdown
    """

    def extendMarkdown(self, md, md_globals):
        # Built-in extensions
        FencedCodeExtension().extendMarkdown(md, md_globals)
        SmartEmphasisExtension().extendMarkdown(md, md_globals)
        TableExtension().extendMarkdown(md, md_globals)

        #gfm.AutolinkExtension().extendMarkdown(md, md_globals)
        #gfm.AutomailExtension().extendMarkdown(md, md_globals)
        #gfm.HiddenHiliteExtension([
        #    ('guess_lang', 'False'),
        #    ('css_class', 'highlight')
        #]).extendMarkdown(md, md_globals)
        #gfm.SemiSaneListExtension().extendMarkdown(md, md_globals)
        #gfm.SpacedLinkExtension().extendMarkdown(md, md_globals)
        #gfm.StrikethroughExtension().extendMarkdown(md, md_globals)
        # Custom extensions
        AutolinkExtension().extendMarkdown(md, md_globals)
        AutomailExtension().extendMarkdown(md, md_globals)
        HiddenHiliteExtension([
            ('guess_lang', 'False'),
            ('css_class', 'highlight')
        ]).extendMarkdown(md, md_globals)
        SemiSaneListExtension().extendMarkdown(md, md_globals)
        SpacedLinkExtension().extendMarkdown(md, md_globals)
        StrikethroughExtension().extendMarkdown(md, md_globals)
        

class GithubFlavoredMarkdownExtension(PartialGithubFlavoredMarkdownExtension):
    """An extension that's as compatible as possible with GFM.
    This extension aims to be compatible with the standard GFM that GitHub uses
    for comments and issues. It has all the extensions described in the `GFM
    documentation`_, except for intra-Github links to commits, repostiories, and
    issues.
    Note that Markdown-formatted gists and files (including READMEs) on GitHub
    use a slightly different variant of GFM. For that, use
    :class:`~mdx_partial_gfm.PartialGithubFlavoredMarkdownExtension`.
    """

    def extendMarkdown(self, md, md_globals):
        PartialGithubFlavoredMarkdownExtension.extendMarkdown(self, md, md_globals)

        Nl2BrExtension().extendMarkdown(md, md_globals)
