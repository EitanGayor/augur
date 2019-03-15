suite = {
    "mxversion" : "5.174.0",
    "name" : "nodeprof",

  "imports" : {
      "suites" : [
          {
              "name" : "graal-nodejs",
              "version" : "9a6cd9fc91dd8a516f18882d32321e293f118bdf",
              "subdir" : True,
              "urls" : [
                  {"url" : "https://github.com/graalvm/graaljs.git", "kind" : "git"},
              ]
          }
      ],
  },

  "developer" : {
      "name" : "Haiyang Sun",
      "email" : "haiyang.sun@usi.ch",
      "organization" : "USI",
      "organizationUrl" : "http://www.inf.usi.ch/",
  },

  "licenses" : {
      "Apache" : { 
          "name" : "Apache License, Version 2.0",
          "url" : "http://www.apache.org/licenses/LICENSE-2.0",
      },
  },

  "defaultLicense" : "Apache",

  "libraries" : {
      "GSON" : {
          "sha1" : "f645ed69d595b24d4cf8b3fbb64cc505bede8829",
          "maven" : {
              "groupId" : "com.google.code.gson",
              "artifactId" : "gson",
              "version" : "2.8.5",
          },
      },
      "GUAVA" : {
          "sha1" : "e47b59c893079b87743cdcfb6f17ca95c08c592c",
          "maven" : {
              "groupId" : "com.google.guava",
              "artifactId" : "guava",
              "version" : "27.1-jre",
          },
      },
  },

  "projects" : {
      "ch.usi.inf.nodeprof" : {
          "subDir" : "src",
          "sourceDirs" : ["src"],
          "dependencies" : [
              "graal-js:GRAALJS",
              "GSON",
              "GUAVA",
          ],
          "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
          "javaCompliance" : "1.8",
          "workingSets" : "Truffle,JavaScript",
          "checkstyle" : "com.oracle.truffle.js.runtime",      
      },
      "ch.usi.inf.nodeprof.test" : {
          "subDir" : "src",
          "sourceDirs" : ["src"],
          "dependencies" : [
              "ch.usi.inf.nodeprof",
              "mx:JUNIT",
              "GSON",
              "GUAVA",
          ],
          "annotationProcessors" : ["truffle:TRUFFLE_DSL_PROCESSOR"],
          "javaCompliance" : "1.8",
          "workingSets" : "Truffle,JavaScript,Test",
      },
  },

  "distributions" : {
      "NODEPROF" : {
          "path" : "build/nodeprof.jar",
          "sourcesPath" : "build/nodeprof.src.zip",
          "dependencies" : [
              "ch.usi.inf.nodeprof",
              "GSON",
              "GUAVA",
          ],
          "distDependencies" : [
              "graal-js:GRAALJS",
              "GSON",
              "GUAVA",
          ],
          "description" : "NodeProf for Graal Node.js",
          "maven" : {
              "artifactId" : "nodeprof",
          }
      },
      "NODEPROF-TEST" : {
          "path" : "build/nodeprof-test.jar",
          "sourcesPath" : "build/nodeprof-test.src.zip",
          "dependencies" : [
              "ch.usi.inf.nodeprof.test",
              "GSON",
              "GUAVA",
          ],
          "distDependencies" : [
              "ch.usi.inf.nodeprof",
              "graal-js:GRAALJS",
              "GSON",
              "GUAVA",
          ],
          "description" : "NodeProf Tests",
          "maven" : {
              "artifactId" : "nodeprof-test",
          }
      },
      "NODEPROF_GRAALVM_SUPPORT" : {
          "native" : True,
          "description" : "NodeProf support distribution for the GraalVM",
          "layout" : {
              "./" : [
                  "file:mx.nodeprof/native-image.properties",
                  "file:README.md",
                  "file:Tutorial.md",
              ],
          },
      },
  },
}
