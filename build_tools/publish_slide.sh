#!/bin/bash

slides_file="${1}"
slides_dir="${2}"

build_file="build.html"
export_file="index.html"

build_dir="${HOME}/dg-src/build/html/slides/${slides_dir}"
pub_dir="${HOME}/dg/docs/slides"
build_script="${HOME}/dg-src/build_tools/org_html_to_revealjs.py"

mv "${slides_file}" "${build_dir}/${build_file}"
cd "${build_dir}/"
"${build_script}" "${build_file}" "${export_file}"
mv "${export_file}" "${pub_dir}/${slides_dir}"
