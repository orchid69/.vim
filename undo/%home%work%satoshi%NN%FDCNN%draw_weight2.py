Vim�UnDo� �a�
����vF��&��������t�   #   ;    ax = fig.add_subplot(4, 4, i + 1, xticks=[], yticks=[])             !       !   !   !    X��A    _�                            ����                                                                                                                                                                                                                                                                                                                                                             X��s     �   
            model = net.ConvTest()5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                                             X���     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���     �               8model = L.Classifier(net.BinaryNetMnist(1,16,32,256,10))5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���     �               'serializers.load_npz("mlp.model",model)5�_�                       G    ����                                                                                                                                                                                                                                                                                                                                                             X���     �             �             5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             X���     �               Pserializers.load_npz("log/BinaryNetMnist-bst-b/BinaryNetMnist16_32.model",model)5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             X���     �               Pserializers.load_npz("log/BinaryNetMnist-bst-b/BinaryNetMnist16_32.model",model)5�_�      	                 S    ����                                                                                                                                                                                                                                                                                                                                                             X���    �               Tserializers.load_npz("log/BinaryNetMnist-bst-bn-fb/BinaryNetMnist16_32.model",model)5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             X��K     �             �             5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             X��P     �               import chainer.functions as F5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             X��Y    �               import chainer.links as F5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        X��m     �                print model.conv1.W.data.shape5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        X��m     �                 # print model.conv1.W.data.shape5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        X��n    �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���    �               'n1, n2, h, w = model.conv1.W.data.shape5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���    �               T    ax.imshow(model.conv1.W.data[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        X��1    �                Ofig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        X���     �               <    ax = fig.add_subplot(2, 10, i + 1, xticks=[], yticks=[])5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        X���    �               <    ax = fig.add_subplot(4, 10, i + 1, xticks=[], yticks=[])5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        X��>     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        X��D   	 �               1n1, n2, h, w = model.predictor.conv1.W.data.shape5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        X���     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       X���     �                ^    ax.imshow(model.predictor.conv1.W.data[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')5�_�                       ]    ����                                                                                                                                                                                                                                                                                                                                                V       X���   
 �               ^    ax.imshow(model.predictor.conv1.W.data[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       X��     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       X��     �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       X��!     �         #      (print model.predictor.conv1.W.data.shape5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                V       X��#     �         #      1n1, n2, h, w = model.predictor.conv1.W.data.shape5�_�                    !   $    ����                                                                                                                                                                                                                                                                                                                                                V       X��%     �       "   #      `    # ax.imshow(model.predictor.conv1.W.data[i, 0], cmap=plt.cm.gray_r, interpolation='nearest')5�_�                    "   "    ����                                                                                                                                                                                                                                                                                                                                                V       X��'     �   !   #   #      E    ax.imshow(model.predictor.conv1.W.data[i, 0], cmap=plt.cm.gray_r)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       X��0     �          #      for i in range(n1):5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                V       X��5     �          #      for i in range(n2):5�_�                   !           ����                                                                                                                                                                                                                                                                                                                                                V       X��@    �      !   #      ;    ax = fig.add_subplot(4, 4, i + 1, xticks=[], yticks=[])5��