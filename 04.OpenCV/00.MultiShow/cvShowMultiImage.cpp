void cvShowMultiImages(char* title,int nChannels, int nArgs, ...) 
{
    IplImage* img;      // img - Used for getting the arguments  
    IplImage* DispImage;// DispImage - the image in which all the input images are to be copied
    int size_r,size_c;  // size - the size of the images in the window
    int ind;            // ind - the index of the image shown in the window
    int x_c, y_r;       // x_c,y_r - the coordinate of top left coner of input images
    int w, h;           // w,h - the width and height of the image
    int r, c;           // r - row , c - col 
    int space_r,space_c;// space - the spacing between images
    if(nArgs <= 0) {    // If argc < 0 or argc > 12 , return without displaying 
        printf("Number of arguments too small..../n");
        return;
    }
    else if(nArgs > 12) {
        printf("Number of arguments too large..../n");
        return;
    }
    // Determine the size of the image, 
    // and the number of rows/cols 
    // from number of arguments 
    else if (nArgs == 1) {
        r = c = 1;
        size_r = 480; size_c = 640 ; 
    }
    else if (nArgs == 2) { // x_c = size_row y_r=size_col
        r = 1; c = 2;
        // size_r = 705; size_c = 350 ; // specail set for show the full story of lena
        size_r = 405; size_c = 540 ; 
    }
    else if ( nArgs == 3 || nArgs == 4) {
        r = 2; c = 2;
        size_r = 405; size_c =540 ; 
    }
    else if (nArgs == 5 || nArgs == 6) {
        r = 2; c = 3;
        size_r = 360; size_c = 480;
    }
    else if (nArgs == 7 || nArgs == 8) {
        r = 2; c = 4;
        size_r = 200; size_c = 240;
    }
    else {
        r = 3; c = 4;
        size_r = 150; size_c = 200; 
    }
    // Create a new 3 channel image to show all the input images 
    // cvSize(width,height)=(col,row)=(y_r,x_c) 
    DispImage = cvCreateImage( cvSize(30 + size_c*c,40 + size_r*r), IPL_DEPTH_8U, nChannels );
    // Used to get the arguments passed
    va_list args;
    va_start(args, nArgs); // stdarg.h
    // Loop for nArgs number of arguments
    space_r = 40/(r+1);
    space_c = 30/(c+1);
    for (ind = 0, x_c = space_c, y_r = space_r; ind < nArgs; ind++, x_c += (space_c + size_c)) {
        // Get the Pointer to the IplImage
        img = va_arg(args, IplImage*);  // stdarg.h
        if(img == 0) {// If img == NULL, release the image, and return
            printf("Invalid arguments");
            cvReleaseImage(&DispImage);
            return;
        }
        // Find the width and height of the image
        w = img->width;
        h = img->height;
        // Used to Align the images
        // i.e. Align the image to next row e.g.r=1,c=2, this row is end , we have ind%c==0 ,
        // then we move to the next row,even the next row can't through the cond  ind < nArgs
        if( ind % c == 0 && x_c!= space_c) {
            x_c  = space_c;
            y_r += space_r + size_r;
        }
        cvSetImageROI(DispImage, cvRect(x_c, y_r, size_c, size_r)); // Set the image ROI to display the current image
        cvResize(img, DispImage);   // Resize the input image and copy the it to the Single Big Image
        cvResetImageROI(DispImage); // Reset the ROI in order to display the next image
    }
    cvNamedWindow( title, 1 );      // Create a new window, and show the Single Big Image
    cvShowImage( title, DispImage);
    cvWaitKey(0);
    va_end(args);                   // End the number of arguments
    cvReleaseImage(&DispImage);     // Release the Image Memory
}