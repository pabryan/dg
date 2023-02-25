(use-package org-special-block-extras.el)

(org-defblock env (type) (title "")
  "Create an environment with a title."
  (format (if (equal backend 'html)
              "<div class=\"%s card my-3 mx-0\"><div class=\"card-header text-white\" style=\"background-color: #0059b3;\"><h5 class=\"card-title\">Definition: %s</h5></div><div class=\"card-body\">%s</div></div>"
            "\\begin{%s}[%s] %s \\end{%s}")
          type title contents type))
