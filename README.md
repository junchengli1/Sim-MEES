# Sim-MEES: Modular End-Effector System Grasping Dataset for Mobile Manipulators in Cluttered Environments
This is the sample dataset part for our paper: [Sim-MEES](https://drive.google.com/drive/folders/1CsWiaqe5LZzFyYPZLGWx-tOw7704hXul?usp=share_link)

seg_dic - object segmentation dictionary.

mass_dic - object mass dictionary.

difficulty_dic - object difficulty level dictionary.


/Stage_0: 

/depth - (800 frames) depth images

/bbox_3d - (800 frames) 3d bounding box 

/bbox_2d_tight - (800 frames) 2d bounding box 

/instance - (800 frames) segmentation mask 

/rgb - (800 frames) RGB image 

/camera_info - Camera matrix

0.npz - point clouds, surface normals, and segmentation ID for each point.

/.*pcd - point cloud of each objects in the cluttered enviroments.

stage_0.usd - cluttered environments usd file.

(1.5 cm suction cup gripper) stage_0_candidates_after_seal.pkl 
```
["segmentation_id"]
["object_name"]
["rotation_after_seal_pass"]
["translation_after_seal_pass"]
["rotation_after_seal_fail"]
["translation_after_seal_fail"]
["translation_after_collision_pass"]
["rotation_after_collision_pass"]
["translation_after_collision_fail"]
["rotation_after_collision_fail"]
["total_candidates"] 
["total_candidates_pass_collision"]
["total_candidates_pass_seal"]
```
(1.5 cm suction cup gripper) stage_0_seal_simulation_candidates.pkl
```
["rotation_after_exp_success"]
["translation_after_exp_success"]
["rotation_after_exp_fail"]
["translation__after_exp_fail"]
["object_mass"]
```


(2.5 cm suction cup gripper) stage_0_candidates_after_seal_2.5cm.pkl  
```
["segmentation_id"]
["object_name"]
["rotation_after_seal_pass"]
["translation_after_seal_pass"]
["rotation_after_seal_fail"]
["translation_after_seal_fail"]
["translation_after_collision_pass"]
["rotation_after_collision_pass"]
["translation_after_collision_fail"]
["rotation_after_collision_fail"]
["total_candidates"] 
["total_candidates_pass_collision"]
["total_candidates_pass_seal"]
```
(2.5 cm suction cup gripper) stage_0_seal_simulation_candidates_2.5cm.pkl
```
["rotation_after_exp_success"]
["translation_after_exp_success"]
["rotation_after_exp_fail"]
["translation__after_exp_fail"]
["object_mass"]
```
(Fetch) stage_0_grasp_candidates_after_overlap.pkl
```
["segmentation_id"]
["object_name"]
["rotation_after_overlap_pass"]
["translation_after_overlap_pass"]
["rotation_after_overlap_fail"]
["translation_after_overlap_fail"]
["total_candidates"]
["total_candidates_pass_overlap"] 

```



