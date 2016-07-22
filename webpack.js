var webpack = require('webpack');
var WebpackDevServer = require('webpack-dev-server');
var config = require('./webpack.config');


new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  stats: true,
  colors: true,
  watchOptions: {
    poll: 1000
  }
}).listen(8001, '0.0.0.0', function (err) {
  if (err) console.log(err);
  console.log('Listening at 0.0.0.0:8001');
});
