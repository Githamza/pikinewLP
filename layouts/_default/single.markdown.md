{{- /*
  Markdown for Agents: single-page output.
  Emitted as index.md alongside index.html so Apache can content-negotiate
  based on the Accept: text/markdown request header.
*/ -}}
# {{ .Title }}

{{- with .Description }}

> {{ . }}
{{- end }}
{{- if not .Date.IsZero }}

_{{ .Date.Format "2 January 2006" }}_
{{- end }}
{{- with .Params.tags }}

**Tags:** {{ delimit . ", " }}
{{- end }}

{{ .RawContent }}
