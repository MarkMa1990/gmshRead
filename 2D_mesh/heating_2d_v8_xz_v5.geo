len_x = 200;
len_y_tio2 = 0.4;
len_y = 50;

mesh_x = 200;
mesh_y_tio2 = 4;
mesh_y = 30;


//
Point(1) = {-len_x/2, 0, 0, 0.0};
Point(2) = {len_x/2, 0, 0, 0.0};

Line(1) = {1, 2};

//+
Extrude {0, -len_y_tio2, 0} {
  Line{1};
  Layers{mesh_y_tio2};
  Recombine;
}


//+
Extrude {0, -len_y, 0} {
  Line{2};
}


//+
Transfinite Line {1, 2, 6} = mesh_x Using Progression 1;
//+
Transfinite Line {7, 8} = mesh_y Using Progression 1;
//+
Transfinite Line {3, 4} = mesh_y_tio2 Using Progression 1;
//+
Transfinite Surface {5};
//+
Transfinite Surface {9};
//+
Recombine Surface {5};
//+
Recombine Surface {9};


//+
Physical Line(10) = {1};

//+ This is a Boundary
Physical Line(11) = {3, 7, 6, 8, 4};
//+
Physical Surface(12) = {9, 5};


