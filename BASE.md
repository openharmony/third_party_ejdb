# EJDB 2.0

[![Join Telegram](https://img.shields.io/badge/join-ejdb2%20telegram-0088cc.svg)](https://tlg.name/ejdb2)
[![license](https://img.shields.io/github/license/Softmotions/ejdb.svg)](https://github.com/Softmotions/ejdb/blob/master/LICENSE)
![maintained](https://img.shields.io/maintenance/yes/2022.svg)

EJDB2 is an embeddable JSON database engine published under MIT license.

[The Story of the IT-depression, birds and EJDB 2.0](https://medium.com/@adamansky/ejdb2-41670e80897c)

* C11 API
* Single file database
* Online backups support
* 500K library size for Android
* [iOS](https://github.com/Softmotions/EJDB2Swift) / [Android](https://github.com/Softmotions/ejdb/tree/master/src/bindings/ejdb2_android/test) / [React Native](https://github.com/Softmotions/ejdb/tree/master/src/bindings/ejdb2_react_native) / [Flutter](https://github.com/Softmotions/ejdb/tree/master/src/bindings/ejdb2_flutter) integration
* Simple but powerful query language (JQL) as well as support of the following standards:
  * [rfc6902](https://tools.ietf.org/html/rfc6902) JSON Patch
  * [rfc7386](https://tools.ietf.org/html/rfc7386) JSON Merge patch
  * [rfc6901](https://tools.ietf.org/html/rfc6901) JSON Path
* [Support of collection joins](#jql-collection-joins)
* Powered by [iowow.io](http://iowow.io) - The persistent key/value storage engine
* HTTP REST/Websockets endpoints powered by [IWNET](https://github.com/Softmotions/iwnet) and [BearSSL](https://github.com/Softmotions/BearSSL).
* JSON documents are stored in using fast and compact [binn](https://github.com/liteserver/binn) binary format

---
* [Native language bindings](#native-language-bindings)
* Supported platforms
  * [macOS](#osx)
  * [iOS](https://github.com/Softmotions/EJDB2Swift)
  * [Linux](#linux)
  * [Android](#android)
  * [Windows](#windows)
* **[JQL query language](#jql)**
  * [Grammar](#jql-grammar)
  * [Quick into](#jql-quick-introduction)
  * [Data modification](#jql-data-modification)
  * [Projections](#jql-projections)
  * [Collection joins](#jql-collection-joins)
  * [Sorting](#jql-sorting)
  * [Query options](#jql-options)
* [Indexes and performance](#jql-indexes-and-performance-tips)
* [Network API](#http-restwebsocket-api-endpoint)
  * [HTTP API](#http-api)
  * [Websockets API](#websocket-api)
* [C API](#c-api)
* [License](#license)
---

[![EJDB2 Presentation](https://iowow.softmotions.com/articles/ejdb-presentation-cover.png)](https://iowow.softmotions.com/articles/ejdb/)

## EJDB2 platforms matrix

|              | Linux              | macOS               | iOS                | Android            | Windows            |
| ---          | ---                | ---                 | ---                | ---                | ---                |
| C library    | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:<sup>1</sup> |
| NodeJS       | :heavy_check_mark: | :heavy_check_mark:  |                    |                    | :x:<sup>3</sup>    |
| DartVM       | :heavy_check_mark: | :heavy_check_mark:<sup>2</sup> |         |                    | :x:<sup>3</sup>    |
| Flutter      |                    |                     | :heavy_check_mark: | :heavy_check_mark: |                    |
| React Native |                    |                     | :x:<sup>4</sup>    | :heavy_check_mark: |                    |
| Swift        | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: |                    |                    |
| Java         | :heavy_check_mark: | :heavy_check_mark:  |                    | :heavy_check_mark: | :heavy_check_mark:<sup>2</sup> |


<br> `[1]` No HTTP/Websocket support [#257](https://github.com/Softmotions/ejdb/issues/257)
<br> `[2]` Binaries are not distributed with dart `pub.` You can build it [manually](https://github.com/Softmotions/ejdb/tree/master/src/bindings/ejdb2_node#how-build-it-manually)
<br> `[3]` Can be build, but needed a linkage with windows node/dart `libs`.
<br> `[4]` Porting in progress [#273](https://github.com/Softmotions/ejdb/issues/273)

## Native language bindings

* [NodeJS](https://www.npmjs.com/package/ejdb2_node)
* [Dart](https://pub.dartlang.org/packages/ejdb2_dart)
* [Java](https://github.com/Softmotions/ejdb/blob/master/src/bindings/ejdb2_jni/README.md)
* [Android support](#android)
* [Swift | iOS](https://github.com/Softmotions/EJDB2Swift)
* [React Native](https://github.com/Softmotions/ejdb/tree/master/src/bindings/ejdb2_react_native)
* [Flutter](https://github.com/Softmotions/ejdb/tree/master/src/bindings/ejdb2_flutter)

### Unofficial EJDB2 language bindings

* Go
  * https://github.com/memmaker/go-ejdb2
* Rust 
  * https://crates.io/crates/ejdb2
* .Net
  * https://github.com/kmvi/ejdb2-csharp
* Haskell
  * https://github.com/cescobaz/ejdb2haskell
  * https://hackage.haskell.org/package/ejdb2-binding
* [Pharo](https://pharo.org)
  * https://github.com/pharo-nosql/pharo-ejdb
* Lua
  * https://github.com/chriku/ejdb-lua

## Status

* **EJDB 2.0 core engine is well tested and used in various heavily loaded deployments**
* Tested on `Linux`, `macOS` and `FreeBSD`. [Has limited Windows support](./WINDOWS.md)
* Old EJDB 1.x version can be found in separate [ejdb_1.x](https://github.com/Softmotions/ejdb/tree/ejdb_1.x) branch.
  We are not maintaining ejdb 1.x.

## Used by

* [Wirow video conferencing platform](https://github.com/wirow-io/wirow-server/)

Are you using EJDB? [Let me know!](mailto:info@softmotions.com)

## macOS

EJDB2 code ported and tested on `High Sierra` / `Mojave` / `Catalina`

[EJDB2 Swift binding](https://github.com/Softmotions/EJDB2Swift) for MacOS, iOS and Linux. 
Swift binding is outdated at now. Looking for contributors.

```
brew install ejdb
```

## Building from sources 

cmake v3.12 or higher required

```
git clone --recurse-submodules git@github.com:Softmotions/ejdb.git

mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make install
```

## Linux

#### Building debian packages

```sh
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DPACKAGE_DEB=ON
make package
```

#### RPM based Linux distributions
```sh
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DPACKAGE_RPM=ON
make package
```

## Windows
EJDB2 can be cross-compiled for windows

**Note:** HTTP/Websocket network API is disabled and not yet supported

Nodejs/Dart bindings not yet ported to Windows.

**[Cross-compilation Guide for Windows](./WINDOWS.md)**


## IWSTART

IWSTART is an automatic CMake initial project generator for C projects based on [iowow](https://github.com/Softmotions/iowow) / [iwnet](https://github.com/Softmotions/iwnet) / [ejdb2](https://github.com/Softmotions/ejdb) libs.

https://github.com/Softmotions/iwstart
