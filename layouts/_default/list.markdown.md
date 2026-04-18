{{- /*
  Markdown for Agents: section/list output.
  Provides a markdown index of the section for agent consumption.
*/ -}}
# {{ .Title }}

{{- with .Description }}

> {{ . }}
{{- end }}

{{ .RawContent }}

{{- if .Pages }}

## Pages

{{ range .Pages -}}
- [{{ .Title }}]({{ .Permalink }}){{ with .Description }} — {{ . }}{{ end }}
{{ end }}
{{- end }}
