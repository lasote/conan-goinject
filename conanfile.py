from conans import ConanFile


class InjectConan(ConanFile):
    name = "go-inject"
    version = "1.0"
    url = "https://github.com/lasote/conan-goinject"

    def source(self):
        self.run("git clone https://github.com/codegangsta/inject.git")
        self.run("cd inject && git checkout v1.0-rc1")  # TAG v1.0-rc1

    def package(self):
        self.copy(pattern='*', dst='src/github.com/codegangsta/inject', src="inject", keep_path=True)
