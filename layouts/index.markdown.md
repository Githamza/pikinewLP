{{- /*
  Markdown for Agents: homepage output.
  Surfaces the site identity, tagline, and a navigable index of sections
  and pages so agents can discover the full site structure.
*/ -}}
# {{ .Site.Title }}

{{- with .Site.Params.description | default .Description }}

> {{ . }}
{{- end }}

{{- with .Params.hero.subtitle }}

{{ . }}
{{- end }}

{{ .RawContent }}

{{- $sections := where .Site.Sections "Params.hidden" "!=" true }}
{{- if $sections }}

## Sections

{{ range $sections -}}
- [{{ .Title }}]({{ .Permalink }}){{ with .Description }} — {{ . }}{{ end }}
{{ end }}
{{- end }}

{{- $pages := where .Site.RegularPages "Params.hidden" "!=" true }}
{{- if $pages }}

## Pages

{{ range $pages -}}
- [{{ .Title }}]({{ .Permalink }}){{ with .Description }} — {{ . }}{{ end }}
{{ end }}
{{- end }}
