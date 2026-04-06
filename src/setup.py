from setuptools import setup
import setup_translate

pkg = 'Extensions.WebAdmin'
setup(name='enigma2-plugin-extensions-webadmin',
       version='3.0',
       description='Extension for enigma2 webinterface to install Ipkgs telnet client',
       package_dir={pkg: 'WebAdmin'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'maintainer.info', 'mobile/*.xml', 'web/*.xml', 'web-data/*.js', 'web-data/*.html', 'web-data/*.jar', 'web-data/img/*.png', 'web-data/tpl/*.htm', 'web-data/tpl/*.css']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
