{
  'variables': {
    'fftwversion': '3.3.4'
  }, 
  'targets': [

  {
    'target_name': 'reodft', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/rdft',
      'fftw-<(fftwversion)/rdft/scalar'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel',
      '<(module_root_dir)/deps/fftw3.gyp:rdft'
    ],
    'sources': [
      'fftw-<(fftwversion)/reodft/conf.c',
      'fftw-<(fftwversion)/reodft/reodft.h',
      'fftw-<(fftwversion)/reodft/reodft010e-r2hc.c',
      'fftw-<(fftwversion)/reodft/reodft11e-radix2.c',
      'fftw-<(fftwversion)/reodft/reodft11e-r2hc-odd.c',
      'fftw-<(fftwversion)/reodft/redft00e-r2hc-pad.c',
      'fftw-<(fftwversion)/reodft/rodft00e-r2hc-pad.c',
      'fftw-<(fftwversion)/reodft/reodft00e-splitradix.c'
    ]
  },

  {
    'target_name': 'rdft.scalar.r2r', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/rdft',
      'fftw-<(fftwversion)/rdft/scalar'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel'
    ],
    'sources': [
      'fftw-<(fftwversion)/rdft/scalar/r2r/e01_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2r/e10_8.c'
    ]
  },

  {
    'target_name': 'rdft.scalar.r2cb', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/rdft',
      'fftw-<(fftwversion)/rdft/scalar'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel'
    ],
    'sources': [
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_2.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_3.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_5.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_6.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_7.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_9.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_10.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_11.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_12.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_13.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_14.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_15.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_64.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_128.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cb_25.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_2.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_3.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_5.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_6.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_7.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_9.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_10.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_12.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_15.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_64.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb_25.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_5.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hb2_25.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_2.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_3.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_5.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_6.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_7.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_9.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_10.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_12.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_15.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_64.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/r2cbIII_25.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_2.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_6.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_10.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_12.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_2.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_6.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_10.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_12.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb2_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb2_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb2_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb2_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cb2_20.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft2_4.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft2_8.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft2_16.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft2_32.c',
      'fftw-<fftwversion)/rdft/scalar/r2cb/hc2cbdft2_20.c'
    ]
  },

  {
    'target_name': 'rdft.scalar.r2cf', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/rdft',
      'fftw-<(fftwversion)/rdft/scalar'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel'
    ],
    'sources': [
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_2.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_3.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_5.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_6.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_7.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_9.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_10.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_11.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_12.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_13.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_14.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_15.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_64.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_128.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_25.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_30.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_40.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cf_50.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_2.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_3.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_5.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_6.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_7.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_9.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_10.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_12.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_15.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_64.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf_25.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_5.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hf2_25.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_2.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_3.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_5.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_6.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_7.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_9.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_10.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_12.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_15.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_64.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/r2cfII_25.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_2.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_6.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_10.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_12.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_2.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_6.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_10.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_12.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf2_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf2_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf2_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf2_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cf2_20.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft2_4.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft2_8.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft2_16.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft2_32.c',
      'fftw-<(fftwversion)/rdft/scalar/r2cf/hc2cfdft2_20.c'
    ]
  },

  {
    'target_name': 'rdft.scalar', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/rdft'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel',
      '<(module_root_dir)/deps/fftw3.gyp:rdft.scalar.r2cf',
      '<(module_root_dir)/deps/fftw3.gyp:rdft.scalar.r2cb',
      '<(module_root_dir)/deps/fftw3.gyp:rdft.scalar.r2r'
    ],
    'sources': [
      'fftw-<(fftwversion)/rdft/scalar/hb.h',
      'fftw-<(fftwversion)/rdft/scalar/r2cb.h',
      'fftw-<(fftwversion)/rdft/scalar/r2cbIII.h',
      'fftw-<(fftwversion)/rdft/scalar/hf.h',
      'fftw-<(fftwversion)/rdft/scalar/hfb.c',
      'fftw-<(fftwversion)/rdft/scalar/r2c.c',	
      'fftw-<(fftwversion)/rdft/scalar/r2cf.h',
      'fftw-<(fftwversion)/rdft/scalar/r2cfII.h',
      'fftw-<(fftwversion)/rdft/scalar/r2r.c',
      'fftw-<(fftwversion)/rdft/scalar/r2r.h',
      'fftw-<(fftwversion)/rdft/scalar/hc2c.c',
      'fftw-<(fftwversion)/rdft/scalar/hc2cf.h',
      'fftw-<(fftwversion)/rdft/scalar/hc2cb.h'
    ]
  },

  {
    'target_name': 'rdft', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/dft'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel',
      '<(module_root_dir)/deps/fftw3.gyp:dft',
      '<(module_root_dir)/deps/fftw3.gyp:rdft.scalar'
    ],
    'sources': [
      'fftw-<(fftwversion)/rdft/buffered2.c',
      'fftw-<(fftwversion)/rdft/direct2.c',
      'fftw-<(fftwversion)/rdft/nop2.c',
      'fftw-<(fftwversion)/rdft/rank0-rdft2.c',
      'fftw-<(fftwversion)/rdft/rank-geq2-rdft2.c',	
      'fftw-<(fftwversion)/rdft/plan2.c',
      'fftw-<(fftwversion)/rdft/problem2.c',
      'fftw-<(fftwversion)/rdft/solve2.c',
      'fftw-<(fftwversion)/rdft/vrank-geq1-rdft2.c',
      'fftw-<(fftwversion)/rdft/rdft2-rdft.c',		
      'fftw-<(fftwversion)/rdft/rdft2-tensor-max-index.c',
      'fftw-<(fftwversion)/rdft/rdft2-inplace-strides.c',
      'fftw-<(fftwversion)/rdft/rdft2-strides.c',	
      'fftw-<(fftwversion)/rdft/khc2c.c',
      'fftw-<(fftwversion)/rdft/ct-hc2c.h',
      'fftw-<(fftwversion)/rdft/ct-hc2c.c',
      'fftw-<(fftwversion)/rdft/ct-hc2c-direct.c',
      'fftw-<(fftwversion)/rdft/hc2hc.h',
      'fftw-<(fftwversion)/rdft/hc2hc.c',
      'fftw-<(fftwversion)/rdft/dft-r2hc.c',
      'fftw-<(fftwversion)/rdft/dht-r2hc.c',
      'fftw-<(fftwversion)/rdft/dht-rader.c',	
      'fftw-<(fftwversion)/rdft/buffered.c',
      'fftw-<(fftwversion)/rdft/codelet-rdft.h',
      'fftw-<(fftwversion)/rdft/conf.c',
      'fftw-<(fftwversion)/rdft/direct-r2r.c',
      'fftw-<(fftwversion)/rdft/direct-r2c.c',
      'fftw-<(fftwversion)/rdft/generic.c',	
      'fftw-<(fftwversion)/rdft/hc2hc-direct.c',
      'fftw-<(fftwversion)/rdft/hc2hc-generic.c',
      'fftw-<(fftwversion)/rdft/khc2hc.c',
      'fftw-<(fftwversion)/rdft/kr2c.c',
      'fftw-<(fftwversion)/rdft/kr2r.c',
      'fftw-<(fftwversion)/rdft/indirect.c',
      'fftw-<(fftwversion)/rdft/nop.c',	
      'fftw-<(fftwversion)/rdft/plan.c',
      'fftw-<(fftwversion)/rdft/problem.c',
      'fftw-<(fftwversion)/rdft/rank0.c',
      'fftw-<(fftwversion)/rdft/rank-geq2.c',
      'fftw-<(fftwversion)/rdft/rdft.h',
      'fftw-<(fftwversion)/rdft/rdft-dht.c',
      'fftw-<(fftwversion)/rdft/solve.c',		
      'fftw-<(fftwversion)/rdft/vrank-geq1.c',
      'fftw-<(fftwversion)/rdft/vrank3-transpose.c'
    ]
  },

  {
    'target_name': 'dft.scalar.codelets', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/dft',
      'fftw-<(fftwversion)/dft/scalar'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel'
    ],
    'sources': [
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_2.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_3.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_4.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_5.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_6.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_7.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_8.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_9.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_10.c',	
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_11.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_12.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_13.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_14.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_15.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_16.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_32.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_64.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_20.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/n1_25.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_2.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_3.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_4.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_5.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_6.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_7.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_8.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_9.c',	
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_10.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_12.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_15.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_16.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_32.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_64.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_20.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t1_25.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_4.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_8.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_16.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_32.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_64.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_5.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_10.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_20.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/t2_25.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/q1_2.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/q1_4.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/q1_8.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/q1_3.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/q1_5.c',
      'fftw-<(fftwversion)/dft/scalar/codelets/q1_6.c'
    ]
  },

  {
    'target_name': 'dft.scalar', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/dft'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel',
      '<(module_root_dir)/deps/fftw3.gyp:dft.scalar.codelets'
    ],
    'sources': [
      'fftw-<(fftwversion)/dft/scalar/n.c',
      'fftw-<(fftwversion)/dft/scalar/t.c',
      'fftw-<(fftwversion)/dft/scalar/f.h',
      'fftw-<(fftwversion)/dft/scalar/n.h',
      'fftw-<(fftwversion)/dft/scalar/q.h',
      'fftw-<(fftwversion)/dft/scalar/t.h'
    ]
  },

  {
    'target_name': 'dft', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel',
      '<(module_root_dir)/deps/fftw3.gyp:dft.scalar'
    ],
    'sources': [
      'fftw-<(fftwversion)/dft/bluestein.c',
      'fftw-<(fftwversion)/dft/buffered.c',
      'fftw-<(fftwversion)/dft/conf.c',
      'fftw-<(fftwversion)/dft/ct.c',
      'fftw-<(fftwversion)/dft/dftw-direct.c',
      'fftw-<(fftwversion)/dft/dftw-directsq.c',
      'fftw-<(fftwversion)/dft/dftw-generic.c',
      'fftw-<(fftwversion)/dft/dftw-genericbuf.c',
      'fftw-<(fftwversion)/dft/direct.c',
      'fftw-<(fftwversion)/dft/generic.c',
      'fftw-<(fftwversion)/dft/indirect.c',
      'fftw-<(fftwversion)/dft/indirect-transpose.c',
      'fftw-<(fftwversion)/dft/kdft-dif.c',
      'fftw-<(fftwversion)/dft/kdft-difsq.c',
      'fftw-<(fftwversion)/dft/kdft-dit.c',
      'fftw-<(fftwversion)/dft/kdft.c',
      'fftw-<(fftwversion)/dft/nop.c',
      'fftw-<(fftwversion)/dft/plan.c',
      'fftw-<(fftwversion)/dft/problem.c',
      'fftw-<(fftwversion)/dft/rader.c',
      'fftw-<(fftwversion)/dft/rank-geq2.c',
      'fftw-<(fftwversion)/dft/solve.c',
      'fftw-<(fftwversion)/dft/vrank-geq1.c',
      'fftw-<(fftwversion)/dft/zero.c',
      'fftw-<(fftwversion)/dft/codelet-dft.h',
      'fftw-<(fftwversion)/dft/ct.h',
      'fftw-<(fftwversion)/dft/dft.h'
    ]
  },

  {
    'target_name': 'simd-support', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel'
    ],
    'dependencies': [
      '<(module_root_dir)/deps/fftw3.gyp:kernel'
    ],
    'sources': [
      'fftw-<(fftwversion)/simd-support/taint.c',
      'fftw-<(fftwversion)/simd-support/simd-common.h',
      'fftw-<(fftwversion)/simd-support/simd-sse2.h',
      'fftw-<(fftwversion)/simd-support/sse2.c',
      'fftw-<(fftwversion)/simd-support/x86-cpuid.h',
      'fftw-<(fftwversion)/simd-support/amd64-cpuid.h',
      'fftw-<(fftwversion)/simd-support/avx.c',
      'fftw-<(fftwversion)/simd-support/simd-avx.h',
      'fftw-<(fftwversion)/simd-support/altivec.c',
      'fftw-<(fftwversion)/simd-support/simd-altivec.h',
      'fftw-<(fftwversion)/simd-support/neon.c'
      'fftw-<(fftwversion)/simd-support/simd-neon.h'
    ]
  },

  {
    'target_name': 'kernel', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)'
    ],
    'sources': [
      'fftw-<(fftwversion)/kernel/align.c',
      'fftw-<(fftwversion)/kernel/alloc.c',
      'fftw-<(fftwversion)/kernel/assert.c',
      'fftw-<(fftwversion)/kernel/awake.c',
      'fftw-<(fftwversion)/kernel/buffered.c',
      'fftw-<(fftwversion)/kernel/cpy1d.c',
      'fftw-<(fftwversion)/kernel/cpy2d-pair.c',
      'fftw-<(fftwversion)/kernel/cpy2d.c',
      'fftw-<(fftwversion)/kernel/ct.c',
      'fftw-<(fftwversion)/kernel/debug.c',
      'fftw-<(fftwversion)/kernel/extract-reim.c',
      'fftw-<(fftwversion)/kernel/hash.c',
      'fftw-<(fftwversion)/kernel/iabs.c',
      'fftw-<(fftwversion)/kernel/kalloc.c',
      'fftw-<(fftwversion)/kernel/md5-1.c',
      'fftw-<(fftwversion)/kernel/md5.c',
      'fftw-<(fftwversion)/kernel/minmax.c',
      'fftw-<(fftwversion)/kernel/ops.c',
      'fftw-<(fftwversion)/kernel/pickdim.c',
      'fftw-<(fftwversion)/kernel/plan.c',
      'fftw-<(fftwversion)/kernel/planner.c',
      'fftw-<(fftwversion)/kernel/primes.c',
      'fftw-<(fftwversion)/kernel/print.c',
      'fftw-<(fftwversion)/kernel/problem.c',
      'fftw-<(fftwversion)/kernel/rader.c',
      'fftw-<(fftwversion)/kernel/scan.c',
      'fftw-<(fftwversion)/kernel/solver.c',
      'fftw-<(fftwversion)/kernel/solvtab.c',
      'fftw-<(fftwversion)/kernel/stride.c',
      'fftw-<(fftwversion)/kernel/tensor.c',
      'fftw-<(fftwversion)/kernel/tensor1.c',
      'fftw-<(fftwversion)/kernel/tensor2.c',
      'fftw-<(fftwversion)/kernel/tensor3.c',
      'fftw-<(fftwversion)/kernel/tensor4.c',
      'fftw-<(fftwversion)/kernel/tensor5.c',
      'fftw-<(fftwversion)/kernel/tensor7.c',
      'fftw-<(fftwversion)/kernel/tensor8.c',
      'fftw-<(fftwversion)/kernel/tensor9.c',
      'fftw-<(fftwversion)/kernel/tile2d.c',
      'fftw-<(fftwversion)/kernel/timer.c',
      'fftw-<(fftwversion)/kernel/transpose.c',
      'fftw-<(fftwversion)/kernel/trig.c',
      'fftw-<(fftwversion)/kernel/twiddle.c',
      'fftw-<(fftwversion)/kernel/cycle.h',
      'fftw-<(fftwversion)/kernel/ifftw.h'
    ]
  },
  {
    'target_name': 'dft', 
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)',
      'fftw-<(fftwversion)/kernel',
      'fftw-<(fftwversion)/dft'
    ],
    'dependencies' : [
      '<(module_root_dir)/deps/fftw3.gyp:kernel'
    ],
    'sources': [
      'fftw-<(fftwversion)/dft/bluestein.c',
      'fftw-<(fftwversion)/dft/buffered.c',
      'fftw-<(fftwversion)/dft/conf.c',
      'fftw-<(fftwversion)/dft/ct.c',
      'fftw-<(fftwversion)/dft/dftw-direct.c',
      'fftw-<(fftwversion)/dft/dftw-directsq.c',
      'fftw-<(fftwversion)/dft/dftw-generic.c',
      'fftw-<(fftwversion)/dft/dftw-genericbuf.c',
      'fftw-<(fftwversion)/dft/direct.c',
      'fftw-<(fftwversion)/dft/generic.c',
      'fftw-<(fftwversion)/dft/indirect.c',
      'fftw-<(fftwversion)/dft/indirect-transpose.c',
      'fftw-<(fftwversion)/dft/kdft-dif.c',
      'fftw-<(fftwversion)/dft/kdft-difsq.c',
      'fftw-<(fftwversion)/dft/kdft-dit.c',
      'fftw-<(fftwversion)/dft/kdft.c',
      'fftw-<(fftwversion)/dft/nop.c',
      'fftw-<(fftwversion)/dft/plan.c',
      'fftw-<(fftwversion)/dft/problem.c',
      'fftw-<(fftwversion)/dft/rader.c',
      'fftw-<(fftwversion)/dft/rank-geq2.c',
      'fftw-<(fftwversion)/dft/solve.c',
      'fftw-<(fftwversion)/dft/vrank-geq1.c',
      'fftw-<(fftwversion)/dft/zero.c',
      'fftw-<(fftwversion)/dft/codelet-dft.h',
      'fftw-<(fftwversion)/dft/ct.h',
      'fftw-<(fftwversion)/dft/dft.h'
    ]
  },

  {
    'target_name': 'fftw3',
    'type': 'static_library',
    'include_dirs': [
      'config/<(OS)'
        'fftw-<(fftwversion)/api',
        'fftw-<(fftwversion)/kernel',
        'fftw-<(fftwversion)/rdft',
        'fftw-<(fftwversion)/dft',
        'fftw-<(fftwversion)/reodft',
        'fftw-<(fftwversion)'
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        'fftw-<(fftwversion)/api',
        'fftw-<(fftwversion)/kernel',
        'fftw-<(fftwversion)/rdft',
        'fftw-<(fftwversion)/dft',
        'fftw-<(fftwversion)/reodft',
        'fftw-<(fftwversion)'
      ]
    },
    'dependencies' : [
      '<(module_root_dir)/deps/fftw3.gyp:kernel',
      '<(module_root_dir)/deps/fftw3.gyp:dft',
      '<(module_root_dir)/deps/fftw3.gyp:rdft',
      '<(module_root_dir)/deps/fftw3.gyp:reodft',
      '<(module_root_dir)/deps/fftw3.gyp:simd-support'
    ],
    'sources': [
      'fftw-<(fftwversion)/api/fftw3.h',
      'fftw-<(fftwversion)/api/apiplan.c',
      'fftw-<(fftwversion)/api/configure.c',
      'fftw-<(fftwversion)/api/execute-dft-c2r.c',
      'fftw-<(fftwversion)/api/execute-dft-r2c.c',
      'fftw-<(fftwversion)/api/execute-dft.c',
      'fftw-<(fftwversion)/api/execute-r2r.c',
      'fftw-<(fftwversion)/api/execute-split-dft-c2r.c',
      'fftw-<(fftwversion)/api/execute-split-dft-r2c.c',
      'fftw-<(fftwversion)/api/execute-split-dft.c',
      'fftw-<(fftwversion)/api/execute.c',
      'fftw-<(fftwversion)/api/export-wisdom-to-file.c',
      'fftw-<(fftwversion)/api/export-wisdom-to-string.c',
      'fftw-<(fftwversion)/api/export-wisdom.c',
      'fftw-<(fftwversion)/api/f77api.c',
      'fftw-<(fftwversion)/api/flops.c',
      'fftw-<(fftwversion)/api/forget-wisdom.c',
      'fftw-<(fftwversion)/api/import-system-wisdom.c',
      'fftw-<(fftwversion)/api/import-wisdom-from-file.c',
      'fftw-<(fftwversion)/api/import-wisdom-from-string.c',
      'fftw-<(fftwversion)/api/import-wisdom.c',
      'fftw-<(fftwversion)/api/malloc.c',
      'fftw-<(fftwversion)/api/map-r2r-kind.c',
      'fftw-<(fftwversion)/api/mapflags.c',
      'fftw-<(fftwversion)/api/mkprinter-file.c',
      'fftw-<(fftwversion)/api/mkprinter-str.c',
      'fftw-<(fftwversion)/api/mktensor-iodims.c',
      'fftw-<(fftwversion)/api/mktensor-rowmajor.c',
      'fftw-<(fftwversion)/api/plan-dft-1d.c',
      'fftw-<(fftwversion)/api/plan-dft-2d.c',
      'fftw-<(fftwversion)/api/plan-dft-3d.c',
      'fftw-<(fftwversion)/api/plan-dft-c2r-1d.c',
      'fftw-<(fftwversion)/api/plan-dft-c2r-2d.c',
      'fftw-<(fftwversion)/api/plan-dft-c2r-3d.c',
      'fftw-<(fftwversion)/api/plan-dft-c2r.c',
      'fftw-<(fftwversion)/api/plan-dft-r2c-1d.c',
      'fftw-<(fftwversion)/api/plan-dft-r2c-2d.c',
      'fftw-<(fftwversion)/api/plan-dft-r2c-3d.c',
      'fftw-<(fftwversion)/api/plan-dft-r2c.c',
      'fftw-<(fftwversion)/api/plan-dft.c',
      'fftw-<(fftwversion)/api/plan-guru-dft-c2r.c',
      'fftw-<(fftwversion)/api/plan-guru-dft-r2c.c',
      'fftw-<(fftwversion)/api/plan-guru-dft.c',
      'fftw-<(fftwversion)/api/plan-guru-r2r.c',
      'fftw-<(fftwversion)/api/plan-guru-split-dft-c2r.c',
      'fftw-<(fftwversion)/api/plan-guru-split-dft-r2c.c',
      'fftw-<(fftwversion)/api/plan-guru-split-dft.c',
      'fftw-<(fftwversion)/api/plan-many-dft-c2r.c',
      'fftw-<(fftwversion)/api/plan-many-dft-r2c.c',
      'fftw-<(fftwversion)/api/plan-many-dft.c',
      'fftw-<(fftwversion)/api/plan-many-r2r.c',
      'fftw-<(fftwversion)/api/plan-r2r-1d.c',
      'fftw-<(fftwversion)/api/plan-r2r-2d.c',
      'fftw-<(fftwversion)/api/plan-r2r-3d.c',
      'fftw-<(fftwversion)/api/plan-r2r.c',
      'fftw-<(fftwversion)/api/print-plan.c',
      'fftw-<(fftwversion)/api/rdft2-pad.c',
      'fftw-<(fftwversion)/api/the-planner.c',
      'fftw-<(fftwversion)/api/version.c',
      'fftw-<(fftwversion)/api/api.h',
      'fftw-<(fftwversion)/api/f77funcs.h',
      'fftw-<(fftwversion)/api/fftw3.h',
      'fftw-<(fftwversion)/api/x77.h',
      'fftw-<(fftwversion)/api/guru.h',
      'fftw-<(fftwversion)/api/guru64.h',
      'fftw-<(fftwversion)/api/mktensor-iodims.h',
      'fftw-<(fftwversion)/api/plan-guru-dft-c2r.h',
      'fftw-<(fftwversion)/api/plan-guru-dft-r2c.h',
      'fftw-<(fftwversion)/api/plan-guru-dft.h',
      'fftw-<(fftwversion)/api/plan-guru-r2r.h',
      'fftw-<(fftwversion)/api/plan-guru-split-dft-c2r.h',
      'fftw-<(fftwversion)/api/plan-guru-split-dft-r2c.h',
      'fftw-<(fftwversion)/api/plan-guru-split-dft.h',
      'fftw-<(fftwversion)/api/plan-guru64-dft-c2r.c',
      'fftw-<(fftwversion)/api/plan-guru64-dft-r2c.c',
      'fftw-<(fftwversion)/api/plan-guru64-dft.c',
      'fftw-<(fftwversion)/api/plan-guru64-r2r.c',
      'fftw-<(fftwversion)/api/plan-guru64-split-dft-c2r.c',
      'fftw-<(fftwversion)/api/plan-guru64-split-dft-r2c.c',
      'fftw-<(fftwversion)/api/plan-guru64-split-dft.c',
      'fftw-<(fftwversion)/api/mktensor-iodims64.c'
    ]
}]}
