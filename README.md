# Environment setup
## Dependencies
#### 1. CLI11
https://github.com/CLIUtils/CLI11/releases?page=2
```
git clone https://github.com/CLIUtils/CLI11 --recursive

cd CLI11
mkdir build
cd build
cmake ..
make
sudo make install
```
#### 2. Pangolin
https://github.com/stevenlovegrove/Pangolin/releases/tag/v0.6
```
sudo apt install libgl1-mesa-dev
sudo apt install libglew-dev
sudo apt install libpython2.7-dev
sudo apt install pkg-config

git clone https://github.com/stevenlovegrove/Pangolin --recursive

cd Pangolin
mkdir build
cd build
cmake ..
make
sudo make install
```
#### 3.nanoflann
https://github.com/jlblancoc/nanoflann/releases/tag/v1.3.2
```
git clone https://github.com/jlblancoc/nanoflann

cd nanoflann
mkdir build
cd build
cmake ..
make
sudo make install
```
#### 4.Eigen3
```
wget https://gitlab.com/libeigen/eigen/-/archive/3.3.9/eigen-3.3.9.tar.gz
tar xvf eigen-3.3.9.tar.gz

cd eigen-3.3.9
mkdir build
cd build
cmake ..
make
sudo make install
```
#### 5.deepSDF compile
```
mkdir build
cd build
cmake ..
make
sudo make install

```
#### 6.Dataset
1. Original Dataset: https://huggingface.co/datasets/ShapeNet/ShapeNetCore
2. Pre-processed dataset: https://cloud.tsinghua.edu.cn/d/fc0f8f8a63974990a4a5/
#### 6.Dataset layout
```
<data_source_name>/
    .datasources.json
    SdfSamples/
        <dataset_name>/
            <class_name>/
                <instance_name>.npz
    SurfaceSamples/
        <dataset_name>/
            <class_name>/
                <instance_name>.ply
```


