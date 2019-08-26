# Noise plugin for the [Document Image Mocker](https://github.com/maylonpedroso/doc-mocker)

This plugin will add an optional `--noise` argument to the `doc-mocker` CLI.

### Pepper Noise
Adds pepper noise to a random percent of the pixels within the specified range.
Accepts the limits of the range as optional parameters. Default `0:30`.

1. Add pepper noise to a random number between 0% and 30% of the pixels
    ```bash
    doc-mocker ... --noise pepper     
    ```
1. Add pepper noise to a random number between 0% and 10% of the pixels
    ```bash
    doc-mocker ... --noise pepper:10  
    ```
1. Add pepper noise to a random number between 5% and 10% of the pixels
    ```bash
    doc-mocker ... --noise pepper:5:10  
    ```

## Credits

View the full list of [contributors](https://github.com/maylonpedroso/doc-mocker-noise-plugin/graphs/contributors).
[MIT](LICENSE) licensed. 