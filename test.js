var fftw = require('./index');
var test = require('tape');

test('1d dft all ones', function(t) {
  t.plan(1);

  fftw.dft_1d([1, 1, 1, 1], function(err, result) {
    t.equal(result[0].real, 4);
  });
});

test('1d idft one 1', function(t) {
  t.plan(1);

  fftw.idft_1d([1, 0, 0, 0], function(err, result) {
    t.equal(result[0].real, 1);
    t.equal(result[2].real, 1);
  });
});
