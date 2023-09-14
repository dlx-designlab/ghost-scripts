//306
import processing.video.*;

Movie myMovie;
PImage croppedImage; // Variable to store the cropped image
int cropSize = 25; // Size of the cropped image
color electrodemeanColor = color(0, 0, 0); // Variable to store the mean color
int frameCount = 0; // Variable to store the frame count


int[][] electrodesCropCoordinates = {
  {150, 375, cropSize, cropSize}, // Crop 1: (x, y, width, height)
  {225, 315, cropSize, cropSize}, // Crop 2: (x, y, width, height)
  {303, 380, cropSize, cropSize}, // Crop 2: (x, y, width, height)
  // Add more crop coordinates as needed
};

void setup() {
  size(1800, 900);
  background(20);
  myMovie = new Movie(this, "test_vid.mp4");
  myMovie.loop(); // Start playing the video

}

void draw() {
  
  // show the main video
  image(myMovie, 0, 0);  

  for (int i = 0; i < electrodesCropCoordinates.length; i++) {
    int[] coords = electrodesCropCoordinates[i];
    
    croppedImage = myMovie.get(coords[0],coords[1],coords[2],coords[3]);
    // show cropped area
    image(croppedImage, 0, i * cropSize);
    
    // Draw a rectangle around the cropped area
    stroke(0, 255, 0);
    noFill();
    rect(coords[0], coords[1], coords[2], coords[3]);

    // Calculate the mean color of the cropped area
    // And fill a rectangle with the mean color
    electrodemeanColor = calculateMeanColor(croppedImage);
    fill(electrodemeanColor);
    noStroke();
    rect(cropSize, i * cropSize, cropSize, cropSize); 
    
    rect(cropSize/10 * frameCount, 750 + i * cropSize/5, cropSize/10, cropSize/5); 
  }

  
  frameCount++;

  // Print mouse coordinates to the console
  println("Mouse X: " + mouseX + ", Mouse Y: " + mouseY);

}

void movieEvent(Movie m) {
  m.read();
}

//void mousePressed() {
//  if (myMovie.isPlaying()) {
//    myMovie.pause();
//  } else {
//    myMovie.play();
//  }
//}

color calculateMeanColor(PImage img) {
  
    int numPixels = img.pixels.length;
    float totalR = 0;
    float totalG = 0;
    float totalB = 0;
  
    img.loadPixels();
    for (int i = 0; i < numPixels; i++) {
      // https://processing.org/reference/pixels.html
      totalR += red(img.pixels[i]);
      totalG += green(img.pixels[i]);
      totalB += blue(img.pixels[i]);
    }
    updatePixels();  
    float meanR = totalR / numPixels;
    float meanG = totalG / numPixels;
    float meanB = totalB / numPixels;

    color meanColor = color(meanR, meanG, meanB);

    return(meanColor);
  }
