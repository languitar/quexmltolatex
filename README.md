# quexmltolatex

This is a simple hack to convert [queXML](https://quexml.acspri.org.au/) documents describing the structure of questionnaires to LaTeX.
I have used this to present a [LimeSurvey](https://www.limesurvey.org) questionnaire in the appendix of a document.

## Warning

This is an early hack and a lot of things might be missing:
* I have only tested this for my special use case. There are probably a lot of queXML structures that I missed.
* There is no real sanitizing for HTML and LaTeX special characters. Only hacks up to the amount that was necessary for my task.

In case this bothers you, feel free to provide a pull request with the missing bits and pieces.

## License

This library is [free software](https://en.wikipedia.org/wiki/Free_software); you can redistribute it and/or modify it under the terms of the [GNU Lesser General Public License](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) as published by the [Free Software Foundation](https://en.wikipedia.org/wiki/Free_Software_Foundation); either version 3 of the License, or any later version. This work is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU Lesser General Public License](https://www.gnu.org/copyleft/lgpl.html) for more details.
