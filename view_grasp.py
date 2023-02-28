#__author__ = 'Juncheng_Li'
#__contact__ = 'li3670@purdue.edu'

import open3d as o3d
import glob
import pickle
import numpy as np
import sys
import argparse

import copy


parser = argparse.ArgumentParser()
parser.add_argument('--data_set_path', default='/media/juncheng/jason-msral/iros/', help='dataset path [default: choose the parent folder path of stage folder]')
parser.add_argument('--gripper_symbol_path', default="/home/juncheng/Documents/symbol.ply", help='choose the path of symbol gripper [default: Fetch wireframe')

parser.add_argument("--stage_ID", type=int, default=0, help='stage ID number [default: 0]')

parser.add_argument("--mode", default="simulation", choices=["collision","simulation"],help="choose the type of check to visualize")
parser.add_argument("--ground", default=True, choices=[True,False],help="whether to include ground plane")
parser.add_argument("--gripper", default="Fetch",choices=["Fetch","Robotiq"],help="choose parallel jaw gripper")



FLAGS = parser.parse_args()

DATA_ROOT = FLAGS.data_set_path
STAGE_ID=FLAGS.stage_ID
MODE=FLAGS.mode
GROUND_PLANE=FLAGS.ground
GRIPPER=FLAGS.gripper
SYMBOL=FLAGS.gripper_symbol_path

def draw(DATA_ROOT,STAGE_ID,MODE,GROUND_PLANE,GRIPPER,SYMBOL):
    display=[]
    pcd_list=glob.glob(DATA_ROOT+ f"stage_{STAGE_ID}"+"/**/*.pcd", recursive=True)
    if GROUND_PLANE==False:
        pcd_list.remove(DATA_ROOT+ f"stage_{STAGE_ID}"+"/ground.pcd")
    if GRIPPER=="Fetch":
        candidate_overlap_path=DATA_ROOT+f"stage_{STAGE_ID}"+ f"/stage_{STAGE_ID}_grasp_candidates_after_overlap.pkl"
        candidate_simulation_path=DATA_ROOT+f"stage_{STAGE_ID}"+ f"/stage_{STAGE_ID}_grasp_simulation_candidates.pkl"
    elif GRIPPER=="Robotiq":
        candidate_seal_path=DATA_ROOT+f"stage_{STAGE_ID}"+ f"/stage_{STAGE_ID}_grasp_candidates_after_overlap_roq.pkl"
        candidate_simulation_path=DATA_ROOT+f"stage_{STAGE_ID}"+ f"/stage_{STAGE_ID}_grasp_simulation_candidates_roq.pkl"

    with open(candidate_overlap_path, 'rb') as f:
        candidate_overlap= pickle.load(f)
    with open(candidate_simulation_path, 'rb') as f:
        candidate_simulation= pickle.load(f)
    
    hand_mesh=o3d.io.read_triangle_mesh(SYMBOL)


    if MODE=="collision":
        for object_index in candidate_overlap.keys():
            translation_candidates=candidate_overlap[object_index]["translation_after_overlap_pass"]
            rotation_candidates=candidate_overlap[object_index]["rotation_after_overlap_pass"]
            translation_candidates_bad=candidate_overlap[object_index]["translation_after_overlap_fail"]
            rotation_candidates_bad=candidate_overlap[object_index]["rotation_after_overlap_fail"]
            for i in range(len(translation_candidates_bad)):
                t_bad=translation_candidates_bad[i]
                R_bad=rotation_candidates_bad[i]
                collision=True
                T = np.eye(4)
                T[:3, :3] = R_bad
                T[0, 3] = t_bad[0]
                T[1, 3] = t_bad[1]
                T[2, 3] = t_bad[2]
                hand_mesh.paint_uniform_color([0, 0, 0.2])
                mesh_t = copy.deepcopy(hand_mesh).transform(T)
                display.append(mesh_t)

            for i in range(len(translation_candidates)):
                t=translation_candidates[i]
                R=rotation_candidates[i]
                collision=False
                T = np.eye(4)
                T[:3, :3] = R
                T[0, 3] = t[0]
                T[1, 3] = t[1]
                T[2, 3] = t[2]

                hand_mesh.paint_uniform_color([0, 1, 0])
                mesh_t = copy.deepcopy(hand_mesh).transform(T)
                display.append(mesh_t)
                


    if MODE=="simulation":
        for object_index in candidate_simulation.keys():
            translation_candidates=candidate_simulation[object_index]["translation_after_exp_success"]
            rotation_candidates=candidate_simulation[object_index]["rotation_after_exp_success"]
            translation_candidates_bad=candidate_simulation[object_index]["translation__after_exp_fail"]
            rotation_candidates_bad=candidate_simulation[object_index]["rotation_after_exp_fail"]
            for i in range(len(translation_candidates_bad)):
                t_bad=translation_candidates_bad[i]
                R_bad=rotation_candidates_bad[i]
                collision=True
                T = np.eye(4)
                T[:3, :3] = R_bad
                T[0, 3] = t_bad[0]
                T[1, 3] = t_bad[1]
                T[2, 3] = t_bad[2]
                hand_mesh.paint_uniform_color([1, 0, 0])
                mesh_t = copy.deepcopy(hand_mesh).transform(T)
                display.append(mesh_t)

            for i in range(len(translation_candidates)):
                t=translation_candidates[i]
                R=rotation_candidates[i]
                collision=False
                T = np.eye(4)
                T[:3, :3] = R
                T[0, 3] = t[0]
                T[1, 3] = t[1]
                T[2, 3] = t[2]
                hand_mesh.paint_uniform_color([0, 1, 0])
                mesh_t = copy.deepcopy(hand_mesh).transform(T)
                display.append(mesh_t)

    for i in pcd_list:

        pcd = o3d.io.read_point_cloud(i)
        display.append(pcd)

    o3d.visualization.draw_geometries_with_custom_animation(display,width=720,height=720)



if __name__ == "__main__":
    draw(DATA_ROOT,STAGE_ID,MODE,GROUND_PLANE,GRIPPER,SYMBOL)










