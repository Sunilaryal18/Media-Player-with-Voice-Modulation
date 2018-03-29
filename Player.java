package pac;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;

public class Player extends BorderPane{
	
	Media media;
	MediaPlayer player;
	MediaView view;
	Pane mpane;
	MediaBar bar;

	public Player(){
		
	}
	
	public Player (String fileName){
		
		media = new Media(fileName);
		player = new MediaPlayer(media);
		view = new MediaView(player);
		mpane = new Pane();
		
		
		mpane.getChildren().add(view);
		setCenter(mpane);
		
	
		bar = new MediaBar(player);
		setBottom(bar);
		
		
		view.setFitHeight(1080);
		view.setFitWidth(1080);
		
		
		view.setPreserveRatio(true);
		player.play();
		
	}

}