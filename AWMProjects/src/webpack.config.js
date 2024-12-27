const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
  // ...other config options
  optimization: {
    minimize: true,
    minimizer: [
      new CssMinimizerPlugin(),
      new TerserPlugin(),
    ],
  },
};
