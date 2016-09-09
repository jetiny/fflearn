{
  'variables': {
    "rel_dbg" : 1,
  },
  'includes': [
    'conf.gypi',
  ],
  "target_defaults": {
    'type': 'executable',
    "sources": [ "empty.cpp"],
  },
  "targets": [
    {"target_name": "avio_dir_cmd", "sources": [ "../deps/ffmpeg/doc/examples/avio_dir_cmd.c" ]},
    {"target_name": "avio_reading", "sources": [ "../deps/ffmpeg/doc/examples/avio_reading.c" ]},
    {"target_name": "decoding_encoding", "sources": [ "../deps/ffmpeg/doc/examples/decoding_encoding.c" ]},
    {"target_name": "demuxing_decoding", "sources": [ "../deps/ffmpeg/doc/examples/demuxing_decoding.c" ]},
    {"target_name": "extract_mvs", "sources": [ "../deps/ffmpeg/doc/examples/extract_mvs.c" ]},
    {"target_name": "filtering_audio", "sources": [ "../deps/ffmpeg/doc/examples/filtering_audio.c" ]},
    # {"target_name": "filtering_video", "sources": [ "../deps/ffmpeg/doc/examples/filtering_video.c" ]},
    {"target_name": "filter_audio", "sources": [ "../deps/ffmpeg/doc/examples/filter_audio.c" ]},
    # {"target_name": "http_multiclient", "sources": [ "../deps/ffmpeg/doc/examples/http_multiclient.c" ]},
    {"target_name": "metadata", "sources": [ "../deps/ffmpeg/doc/examples/metadata.c" ]},
    {"target_name": "muxing", "sources": [ "../deps/ffmpeg/doc/examples/muxing.c" ]},
    # {"target_name": "qsvdec", "sources": [ "../deps/ffmpeg/doc/examples/qsvdec.c" ]},
    {"target_name": "remuxing", "sources": [ "../deps/ffmpeg/doc/examples/remuxing.c" ]},
    {"target_name": "resampling_audio", "sources": [ "../deps/ffmpeg/doc/examples/resampling_audio.c" ]},
    {"target_name": "scaling_video", "sources": [ "../deps/ffmpeg/doc/examples/scaling_video.c" ]},
    {"target_name": "transcode_aac", "sources": [ "../deps/ffmpeg/doc/examples/transcode_aac.c" ]},
    {"target_name": "transcoding", "sources": [ "../deps/ffmpeg/doc/examples/transcoding.c" ]},
  ]
}
