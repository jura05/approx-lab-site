#!/usr/bin/env python3
# coding: utf-8

import jinja2
import shutil
import os
import os.path

def render():
    dst_dir = '../generated-content'
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    os.mkdir(dst_dir + '/conf2018')
    os.mkdir(dst_dir + '/en')
    os.mkdir(dst_dir + '/en/conf2018')

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./templates'),
    )
    common = [
        'index.html', 'about.html', 'staff.html', 'contacts.html',
        'events.html', 'publications.html',
    ]
    templates = common + ['en/' + t for t in common]
    templates.append('conf2018/index.html')
    conf_tmpl = [
        'index.html', 'committee.html', 'program.html',
        'venue.html', 'participants.html',
    ]
    templates += ['en/conf2018/' + t for t in conf_tmpl]

    for tmpl_name in templates:
        tmpl = env.get_template(tmpl_name)

        if tmpl_name.startswith('en/'):
            chlang_ref = tmpl_name[3:]
        else:
            chlang_ref = 'en/' + tmpl_name

        html = tmpl.render(chlang_ref=chlang_ref)
        with open(dst_dir + '/' + tmpl_name, 'w') as fh:
            fh.write(html)

    shutil.copytree('css', dst_dir + '/css')
    shutil.copytree('media', dst_dir + '/media')
    


if __name__ == "__main__":
    render()
