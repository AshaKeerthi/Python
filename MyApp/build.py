from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pydev")


name = "MyApp"
default_task = ["install_dependencies", "analyze", "publish"]


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
    project.set_property("flake8_exclude_patterns","/target, build.py, setup.py")
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_test_sources', True)
    project.build_depends_on("mock")
