{
  "targets": [
    {
      "target_name": "fftw",
      "sources": [ 
        "src/fftw.cc" 
      , "src/complex.cc"
      , "src/fft_worker.cc"
      , "src/fft_worker_1d.cc"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        [ "OS==\"mac\"",
          {
            "link_settings": {
              "libraries": [
                "-lfftw3", "-lm"
              ]
            }
          }
        ]
      ]
    }
  ]
}
