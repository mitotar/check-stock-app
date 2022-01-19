# check-stock

<img src="sample.gif" style="width:80%"/>

## Automatically check the stock status of products

### Supported websites:

-   <a href="https://www.chapters.indigo.ca/en-ca/">chapters.indigo.ca</a>
-   <a href="https://www.lego.com/en-ca/">lego.com</a>

As this program was primarily created for my own personal use, I currently have no plans of adding support for any more stores.<br>

### To run:

1. Open the terminal and navigate to the `check-stock` folder.
2. Run the following line:
    ```shell
    python3 app.py
    ```
3. To quit the program, press <kbd>⌃ control</kbd> + <kbd>C</kbd> in your terminal, and close the browser window.

### To run on Mac, without terminal (mostly):

1. Open Finder and navigate to the location of this folder (`check-stock`).
2. Double-click the file `app.command`. This will launch your terminal.<br>
    - If this gives you an "unidentified developer" error, right-click the file, choose Open > Open.
3. Displayed in your terminal will be a line similar to the following:
    ```shell
    * Running on http://111.0.0.1:1000/ (Press CTRL+C to quit)
    ```
    Copy this http link into your browser of choice.
4. To quit the program, press <kbd>⌃ control</kbd> + <kbd>C</kbd> in your terminal, and close the browser window.

If you get a permission error at step 2, do the following then continue above with step 3:

1. Open Terminal (<kbd>⌘ command</kbd> + <kbd>space</kbd>, type in 'Terminal', press <kbd>enter</kbd>).
2. Navigate to the `check_stock` folder.
3. Run the following command:
    ```shell
    chmod 111 app.command
    ```

<br><br>

## To-do

1. Update sample gif
2. Create filter to only view products from certain stores (only useful if I add more stores)
3. Add option to change "nickname" of product
4. Automatically run this program every set amount of time and send notification
