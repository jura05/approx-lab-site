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
    os.mkdir(dst_dir + '/sbs100')
    os.mkdir(dst_dir + '/en')
    os.mkdir(dst_dir + '/en/conf2018')
    os.mkdir(dst_dir + '/en/sbs100')

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./templates'),
    )
    common = [
        'index.html', 'about.html', 'staff.html', 'contacts.html',
        'publications.html',
    ]
    russian = ['seminar.html', 'spk2018.html']
    english = []

    conf_tmpl = [
        'index.html', 'committee.html', 'program.html',
        'directions.html', 'participants.html', 'contacts.html',
    ]
    english += ['en/conf2018/' + t for t in conf_tmpl]

    sbs100_tmpl = [
        'index.html',
    ]
    russian += ['sbs100/' + t for t in sbs100_tmpl]
    english += ['en/sbs100/' + t for t in sbs100_tmpl]

    templates = common + ['en/' + t for t in common] + russian + english
    templates.append('conf2018/index.html')

    for tmpl_name in templates:
        tmpl = env.get_template(tmpl_name)

        if tmpl_name in russian:
            chlang_ref = 'en/index.html'
        elif tmpl_name in english:
            chlang_ref = 'index.html'
        elif tmpl_name.startswith('en/'):
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
