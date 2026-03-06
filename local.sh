topreward/scripts/run_predict.sh --config-name predict_topreward \
  data_loader=local \
  dataset=local_video \
  dataset.video_path=./bead.mp4 \
  dataset.instruction="insert all the glass beads equally into slots without pausing" \
  prediction.num_samples=100 \
  prediction.num_examples=1