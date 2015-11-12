# conan-goinject

[Conan.io](https://conan.io) package for [go lib inject library](https://github.com/codegangsta/inject) 

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/inject/1.0/lasote/stable).

## How to use

Install **conan** from [Conan.io](https://conan.io)

Create a *conanfile.txt* file in your project:
    
	[requires]
	inject/1.0@lasote/stable
	
   	[imports]
	src, * -> ./deps/src 


Conan will generate a folder "build" with all your specified requires.

Just put build folder in go path and run your program:

	export GOPATH=${PWD}:${PWD}/deps
	cd src/myfolder
	go run myprogram.go

