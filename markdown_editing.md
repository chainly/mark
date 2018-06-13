# install
> https://www.cnblogs.com/james-lee/p/6847906.html
1. Markdown Editing
2. MarkdownLivePreview

# Q&S
1. Error loading syntax file "Packages/Markdown/Markdown.sublime-syntax": Unable to read Packages/Markdown/Markdown.sublime-syntax
> https://github.com/SublimeText-Markdown/MarkdownEditing/issues/485#markdown

```
As noted by @erikjoling :
This issue occurs when the package is installed when there is a markdown file currently open. All that is needed to fix the problem is to save the markdown file, close it, quit sublime, then reopen the file.
```
