topreward/scripts/run_predict.sh --config-name predict_topreward \
  data_loader=local \
  dataset=local_video \
  dataset.video_path=./REC-20260305221637.mp4 \
  "dataset.instruction='Grasp on to the mug, and place it onto the plate'" \
  prediction.num_samples=100 \
  prediction.num_examples=1