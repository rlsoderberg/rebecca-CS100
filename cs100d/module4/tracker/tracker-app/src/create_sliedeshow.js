import "./styles.css";


const Slide = ({ image_url, caption, active }) => {
  return (
    <div className={`slide ${active ? "active" : ""}`}>
      <img src={this_filename} alt={caption} />
      <span>{caption}</span>
    </div>
  );
};
