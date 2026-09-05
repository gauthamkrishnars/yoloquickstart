from pathlib import Path
from ultralytics import YOLO


def main() -> None:
    # Load the pre-trained YOLOv8 nano model
    model = YOLO("yolov8n.pt")

    # Run inference on the specified image URL
    image_url = "https://ultralytics.com/images/bus.jpg"
    results = model(image_url)

    # Save output image with bounding boxes directly to the root folder as results.jpg
    output_path = Path(__file__).resolve().parent / "results.jpg"
    results[0].save(filename=str(output_path))
    print(f"Detections saved to: {output_path}")


if __name__ == "__main__":
    main()
