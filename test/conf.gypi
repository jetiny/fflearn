{
  'variables': {
    "rel_dbg" : 1,
    "target_arch": "x64",
  },
  "target_defaults":
    {
      'default_configuration': 'Release',
      "conditions": [
          ['target_arch=="x64"', {
            'msvs_configuration_platform': 'x64',
          }],
        ['OS=="win"', {
          'configurations': {
            'Release': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'conditions': [
                    ['rel_dbg==1', {
                      'Optimization': 0,
                      'FavorSizeOrSpeed': 0,
                      'InlineFunctionExpansion': 0,
                      'WholeProgramOptimization': 'false',
                      'OmitFramePointers': 'false',
                      'EnableFunctionLevelLinking': 'false',
                      'EnableIntrinsicFunctions': 'false',
                    }]
                  ],
                },
                'VCLinkerTool': {
                  'conditions': [
                    ['rel_dbg==1', {
                      'LinkTimeCodeGeneration': 0,
                      'OptimizeReferences': 2,
                      'EnableCOMDATFolding': 2,
                      'LinkIncremental': 1
                   }]
                  ],
                }
              }
            }
          },
          "include_dirs": [
            "../deps/ffmpeg/include",
            "../deps/include",
          ],
          "libraries": [
            '../../deps/ffmpeg/lib/avcodec.lib',
            "../../deps/ffmpeg/lib/avdevice.lib",
            "../../deps/ffmpeg/lib/avfilter.lib",
            "../../deps/ffmpeg/lib/avformat.lib",
            "../../deps/ffmpeg/lib/avutil.lib",
            "../../deps/ffmpeg/lib/postproc.lib",
            "../../deps/ffmpeg/lib/swresample.lib",
            "../../deps/ffmpeg/lib/swscale.lib",
          ],
        }]
      ]
    }
}
