(use-package org-special-block-extras)

(org-defblock env (type) (title "")
  "Create an environment with a title."
  (format (if (equal backend 'html)
              (concat "<div class=\"%s card\"><div class=\"card-header\"><h5 class=\"card-title\">" (if (equal title "") "%s" " : %s") "</h5></div><div class=\"card-body\">%s</div></div>")
            "\\begin{%s}[%s] %s \\end{%s}")
	  type title contents type))

(org-defblock notes () ()
  "Environment for speaker notes"
  (format "<aside class=\"notes\">%s</aside>" contents))
