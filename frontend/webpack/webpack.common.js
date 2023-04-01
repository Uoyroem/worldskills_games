const path = require('node:path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: path.resolve(__dirname, '../src/scripts/index.ts'),
    output: {
        path: path.join(__dirname, '../build'),
        filename: 'index.js'
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'index.css'
        })
    ],
    module: {
        rules: [
            {
                test: /\.[tj]s$/,
                loader: 'ts-loader'
            },
            {
                test: /\.(sc|sa|c)ss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: {
                            sourceMap: true
                        }
                    },
                    'sass-loader'
                ]
            },
            {
                test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)$/,
                type: 'asset'
            },
        ]
    }
};
