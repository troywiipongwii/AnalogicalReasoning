
# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops, ImageMath, ImageOps, ImageStat, ImageFilter
import math, operator
import numpy as np
import random


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual Ravensprob_fig, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    skipping= 0
    def Solve(self, problem):
        
        if problem.problemType == '2x2':
            
            print("problem name: " + problem.name)
            prob_fig = {}
            ans_fig = {}
            prob_array = {}
            ans_array = {}
            
            
            rav_list = ['A', 'B', 'C']
            ans_list = ['1', '2', '3', '4', '5', '6']   
    
    
            for key in problem.figures:
                fig = problem.figures[key]
                image = Image.open(fig.visualFilename).convert('1')               
                arrayImage = self.centerImageArray(np.array(image))
                if key in rav_list:
                    prob_fig[key] = image
                    prob_array[key] = arrayImage
                if key in ans_list:
                    ans_fig[key] = image   
                    ans_array[key] = arrayImage          
            
            
            ATransformations = [ 
            prob_fig['A'].transpose(Image.FLIP_LEFT_RIGHT), 
            prob_fig['A'].transpose(Image.FLIP_TOP_BOTTOM), 
            prob_fig['A'].transpose(Image.ROTATE_90), 
            prob_fig['A'].transpose(Image.ROTATE_180), 
            prob_fig['A'].transpose(Image.ROTATE_270)
            ]
            
            BTransformations = [ 
            prob_fig['B'].transpose(Image.FLIP_LEFT_RIGHT), 
            prob_fig['B'].transpose(Image.FLIP_TOP_BOTTOM), 
            prob_fig['B'].transpose(Image.ROTATE_90), 
            prob_fig['B'].transpose(Image.ROTATE_180), 
            prob_fig['B'].transpose(Image.ROTATE_270)
            ]   
            
            CTransformations = [ 
            prob_fig['C'].transpose(Image.FLIP_LEFT_RIGHT), 
            prob_fig['C'].transpose(Image.FLIP_TOP_BOTTOM), 
            prob_fig['C'].transpose(Image.ROTATE_90), 
            prob_fig['C'].transpose(Image.ROTATE_180), 
            prob_fig['C'].transpose(Image.ROTATE_270)
            ]
            
                                           
            if self.equal_images(prob_fig['A'], prob_fig['B'])[0]:
                print('A == B')
                for i in range(1,7):
                    if self.equal_images(ans_fig[str(i)], prob_fig['C'])[0]:
                        answer = i
                        print(answer)
                        return answer                  

                    
            elif self.equal_images(prob_fig['A'], prob_fig['C'])[0]:             
                for i in range(1,7):
                    if self.equal_images(ans_fig[str(i)], prob_fig['B'])[0]:
                        answer = i
                        print(answer)
                        return answer
                    
            elif self.equal_images(prob_fig['B'], self.black_white_pixel_flip(ImageChops.difference(prob_fig['A'],prob_fig['B'])))[0]:
                for i in range(1,9):
                    if self.equal_images(ans_fig[str(i)], self.black_white_pixel_flip(ImageChops.difference(prob_fig['C'],ans_fig[str(i)])))[0]:
                        print(i)
                        return i
                
            elif self.equal_images(prob_fig['C'], self.black_white_pixel_flip(ImageChops.difference(prob_fig['A'],prob_fig['C'])))[0]:
                for i in range(1,9):
                    if self.equal_images(ans_fig[str(i)], self.black_white_pixel_flip(ImageChops.difference(prob_fig['B'],ans_fig[str(i)])))[0]:
                        print(i)
                        return i                   
                                   
            else:
                for x in range(len(ATransformations)):
                    if self.equal_images(ATransformations[x], prob_fig['B'])[0]:
                        trans = x
                        for i in range(1,7):
                            if self.equal_images(ans_fig[str(i)], CTransformations[trans])[0]:
                                print(i)
                                return i
                            
                for x in range(len(ATransformations)):
                    if self.equal_images(ATransformations[x], prob_fig['C'])[0]:
                        trans = x
                        for i in range(1,7):
                            if self.equal_images(ans_fig[str(i)], BTransformations[trans])[0]:
                                print(i)
                                return i              
                             
                else:
                    answer = random.randint(1,7)
                    print(answer)
                    return answer            
        
        
        
        if problem.problemType == '3x3':
            print("problem name: " + problem.name)

            prob_fig = {}
            ans_fig = {}
            prob_array = {}
            ans_array = {}
        
        
            rav_list = ['A', 'B', 'C','D','E','F','G','H']
            ans_list = ['1', '2', '3', '4', '5', '6','7','8']   
        
        
            for key in problem.figures:
                fig = problem.figures[key]
                image = Image.open(fig.visualFilename).convert('1')                   
                arrayImage = self.centerImageArray(np.array(image))
                if key in rav_list:
                    prob_fig[key] = image
                    prob_array[key] = arrayImage
                if key in ans_list:
                    ans_fig[key] = image   
                    ans_array[key] = arrayImage

    
            rowAB = ImageChops.add(prob_fig['A'], prob_fig['B'])
            rowBC = ImageChops.add(prob_fig['B'], prob_fig['C'])
            rowDE = ImageChops.add(prob_fig['D'], prob_fig['E'])
            rowEF = ImageChops.add(prob_fig['E'], prob_fig['F'])
    
            colAD =ImageChops.multiply(prob_fig['A'], prob_fig['D'])
            colADG= ImageChops.multiply(colAD, prob_fig['G'])
    
            colBE =ImageChops.multiply(prob_fig['B'], prob_fig['E'])
            colBEH= ImageChops.multiply(colBE, prob_fig['H'])
    
            ab = ImageChops.multiply(prob_fig['A'],prob_fig['B'])
            bc = ImageChops.multiply(prob_fig['B'], prob_fig['C'])
            ac = ImageChops.multiply(prob_fig['A'],prob_fig['C'])
            df = ImageChops.multiply(prob_fig['D'],prob_fig['F'])
            abc = ImageChops.multiply(ab,prob_fig['C'])
            de = ImageChops.multiply(prob_fig['D'],prob_fig['E'])
            de_F=ImageChops.multiply(de,prob_fig['F'])
            ef = ImageChops.multiply(prob_fig['E'],prob_fig['F'])
    
            difAB=self.black_to_white_pixels(ImageChops.difference(prob_fig['A'], prob_fig['B']))
            difDE=self.black_to_white_pixels(ImageChops.difference(prob_fig['D'], prob_fig['E']))
    
            if self.equal_images(prob_fig['A'], prob_fig['B'])[0] and self.equal_images(prob_fig['B'], prob_fig['C'])[0]:
                if self.equal_images(prob_fig['D'], prob_fig['E'])[0] and self.equal_images(prob_fig['E'], prob_fig['F'])[0]:
                    for i in range(1,9):
                        if self.equal_images(prob_fig['H'],ans_fig[str(i)])[0]:
                            return i
            elif self.equal_images(prob_fig['A'],prob_fig['E'])[0]:
                for i in range(1,9):
                    if self.equal_images(prob_fig['E'],ans_fig[str(i)])[0]:
                        return i        
            elif ((self.equal_images(prob_fig['A'], prob_fig['D'])[0] or self.equal_images(prob_fig['A'], prob_fig['E'])[0] or self.equal_images(prob_fig['A'],prob_fig['F'])[0]) \
                    and (self.equal_images(prob_fig['B'], prob_fig['D'])[0] or self.equal_images(prob_fig['B'], prob_fig['E'])[0] or self.equal_images(prob_fig['B'], prob_fig['F'])[0]) \
                    and (self.equal_images(prob_fig['C'], prob_fig['D'])[0] or self.equal_images(prob_fig['C'], prob_fig['E'])[0] or self.equal_images(prob_fig['C'], prob_fig['F'])[0])):
                if self.equal_images(prob_fig['A'], prob_fig['G'])[0] or self.equal_images(prob_fig['A'],prob_fig['H'])[0]:
                    if self.equal_images(prob_fig['B'], prob_fig['G'])[0] or self.equal_images(prob_fig['B'],prob_fig['H'][0]):
                        if self.equal_images(prob_fig['C'], prob_fig['G'])[0] or self.equal_images(prob_fig['C'],prob_fig['H'])[0]:
                            print("need to chose another strategy")
                        else:
                            missing_figure ='C'
                    else:
                        missing_figure ='B'
                else:
                    missing_figure = "A"
        
                for i in range(1, 9):
                    if self.equal_images(prob_fig[missing_figure], ans_fig[str(i)])[0]:
                        return i            
            
            elif self.equal_images(rowAB, rowBC)[0] and self.equal_images(rowDE, rowEF)[0]:
                rowCF = ImageChops.add(prob_fig["C"], prob_fig["F"])
                rowGH = ImageChops.add(prob_fig["G"], prob_fig["H"])
                rowHF = ImageChops.multiply(prob_fig["H"], prob_fig["F"])
                answers ={}
    
                for i in range(1, 9):
                    candidate = ImageChops.add(rowCF, ans_fig[str(i)])
                    candidate2 = ImageChops.add(rowGH, ans_fig[str(i)])
        
                    if self.equal_images(rowCF, candidate)[0] and self.equal_images(rowGH, candidate2)[0]:
        
                        answers[i]= ans_fig[str(i)]
        
                if len(answers)!=1:
                    if self.transformation_equality(prob_fig):
                        return self.apply_transform(prob_fig, ans_fig)
                    else:
                        return self.no_duplicates(prob_fig, ans_fig)
                else:
                    for keys in answers:
                        answer = answers[keys][0]
                        return answer
                return -1
        
            elif self.equal_images(colADG, colBEH)[0]:
                colAD= ImageChops.multiply(prob_fig['A'], prob_fig['D'])
                colADG= ImageChops.multiply(colAD, prob_fig['G'])
                colCF= ImageChops.multiply(prob_fig['C'], prob_fig['F'])
        
                for i in range(1, 9):
                    candidate = ImageChops.multiply(colCF, ans_fig[str(i)])
                    if self.equal_images(candidate,colADG)[0]:
                        return i
                return -1
            if self.equal_images(ab, prob_fig['C'])[0] and self.equal_images(de, prob_fig['F'])[0]:
                i = 1
                answer = self.combo_answer(prob_fig, ans_fig, i)
                return answer
            elif self.equal_images(ac, prob_fig['B'])[0] and self.equal_images(df, prob_fig['E'])[0]:
                i = 2
                answer = self.combo_answer(prob_fig, ans_fig, i)
                return answer                              
            elif self.equal_images(abc, de_F)[0]:
                i = 0
                answer = self.combo_answer(prob_fig, ans_fig, i)
                return answer                
            elif self.equal_images(difAB, prob_fig['C'])[0] and self.equal_images(difDE, prob_fig['F'])[0]:
                answer = self.ans_difference(prob_fig, ans_fig)
                return answer
            elif self.transformation_equality(prob_fig):
                return self.apply_transform(prob_fig, ans_fig)
            else:
                try:
                    answer = self.no_duplicates(prob_fig, ans_fig)
                    return answer
                except:
                    answer = random.randint(1,9)
                    return answer
    
            return -1


    @staticmethod
    def equal_images(im1, im2):
        dif = sum(abs(p1 - p2) for p1, p2 in zip(im1.getdata(), im2.getdata()))

        ncomponents = im1.size[0] * im1.size[1] * 3
        dist = (dif / 255.0 * 100) / ncomponents
        im1__getcolors = im1.getcolors()
        im2_getcolors = im2.getcolors()
        black1 = (10000, 0)
        if len(im1__getcolors) > 1:
            black, white = im1__getcolors

        else:
            if im1__getcolors[0][1] == 255:
                white = im1__getcolors
                black = (0, 0)
            else:
                black = im1__getcolors
                white = (0, 255)

        if len(im2_getcolors) > 1:
            black1, white1 = im2_getcolors
        else:
            if im2_getcolors[0][1] == 255:
                white1 = im2_getcolors
                black1 = (0, 0)
            else:
                black1 = im2_getcolors
                white1 = (0, 255)



        stats = {"dist": dist, "blk": abs(black[0] - black1[0])}


        return (dist<1.1 and abs(black[0]-black1[0])<105), stats
        # return (dist<1.1 and abs(black[0]-black1[0])<105 and abs(white[0]-white1[0]<100)), stats

    def transformation_equality(self, prob_fig):
        sharedAB=self.pixel_comparison(prob_fig["A"], prob_fig["B"])[0]
        sharedDE=self.pixel_comparison(prob_fig["D"], prob_fig["E"])[0]
        return self.equal_images(sharedAB, prob_fig["C"])[0] and self.equal_images(sharedDE, prob_fig["F"])[0]

    def apply_transform(self, prob_fig, ans_fig):
        sharedGE=self.pixel_comparison(prob_fig["G"], prob_fig["H"])[0]
        for i in range(1, 9):
            if self.equal_images(sharedGE, ans_fig[str(i)])[0]:
                return int(i)
        else:
            try:
                answer = self.no_duplicates(prob_fig, ans_fig)
                return answer
            except:
                answer = random.randint(1,9)
                return answer            
            return -1

    def combo_answer(self, prob_fig, ans_fig, index):
        de = ImageChops.multiply(prob_fig["D"],prob_fig["E"])
        gh = ImageChops.multiply(prob_fig["G"],prob_fig["H"])
        de_F=ImageChops.multiply(de,prob_fig["F"])


        if index == 0:
            for i in range (1,9):
                candidate= ImageChops.multiply(gh, ans_fig[str(i)])
                if self.equal_images(candidate,de_F)[0]:
                    return i
            return self.no_duplicates(prob_fig, ans_fig)
        
        if index == 1:
            for i in range (1,9):
                if self.equal_images(gh,ans_fig[str(i)])[0]:
                    return i
            return self.no_duplicates(prob_fig, ans_fig)
        
        if index == 2:
            for i in range (1,9):
                candidate= ImageChops.multiply(prob_fig["G"], ans_fig[str(i)])
                if self.equal_images(candidate,prob_fig["H"])[0]:
                    return i
            return self.no_duplicates(prob_fig, ans_fig)

    def ans_difference(self, prob_fig, ans_fig):
        difGH=self.black_to_white_pixels(ImageChops.difference(prob_fig["H"], prob_fig["G"]))
        for i in range (1,9):
            if self.equal_images(ans_fig[str(i)],difGH)[0]:
                return i
        return self.no_duplicates(prob_fig, ans_fig)


    def no_duplicates(self, prob_fig, ans_fig):
        figs =["A","B","C","D","E","F","G", "H"]
        answers=[1,2,3,4,5,6,7,8]
        for fig in figs:
            for i in range(1,9):
                if self.equal_images(prob_fig[fig], ans_fig[str(i)])[0] :
                    if i in answers:
                        answers.remove(i)

        if len(answers)==1:
            return answers[0]
        elif self.skipping:
            return -1
        return answers[0]

    
    def black_to_white_pixels(self, image):
        inverted = Image.new("1", image.size, "white")
        for x in range(0, image.size[1]):
            for y in range(0, image.size[0]):
                p1 = image.getpixel((x, y))
                if (p1 == 0):
                    inverted.putpixel((x, y), 255)
                else:
                    inverted.putpixel((x, y), 0)

        return inverted
    
    def centerImageArray(self,figArray):
        figImage = Image.fromarray(figArray, "L")

        # mask
        threshold=128
        mask = figImage.point(lambda p: p < threshold and 255)

        # find edges
        edges = mask.filter(ImageFilter.FIND_EDGES)
        box = edges.getbbox()
        edges = edges.crop(box)

        # center in new image-figure
        tempImg = Image.new("L", figImage.size)

        width, height = edges.size
        fwidth, fheight = figImage.size

        tempImg.paste(edges, ((fwidth - width) // 2, (fheight - height) // 2))

        return np.array(tempImg)    
    
    def pixel_comparison(self, img1, img2):
        common = Image.new("1", img1.size, "white")

        delta = Image.new("1", img1.size, "white")
        for x in range(0, common.size[1]):
            for y in range(0, common.size[0]):
                p1 = img1.getpixel((x, y))
                p2 = img2.getpixel((x, y))
                if (p1 == 0 and p2 == 0):
                    common.putpixel((x, y), 0)

                elif p1 == 255 and p2 == 255:
                    common.putpixel((x, y), 255)

                else:

                    delta.putpixel((x, y), 0)

        return common, delta    
    
    def center_lists(self, list1):
        
        listUpdate = [self.centerImageArray(np.array(list1[x])) for x in range(len(list1))]
        return listUpdate
    
    def black_white_pixel_flip(self, image):
        inverted = Image.new("1", image.size, "white")
        for x in range(0, image.size[1]):
            for y in range(0, image.size[0]):
                p1 = image.getpixel((x, y))
                if (p1 == 0):
                    inverted.putpixel((x, y), 255)
                else:
                    inverted.putpixel((x, y), 0)

        return inverted  
    
    def make_transparent(self,img):

        pixdata = img.load()

        width, height = img.size
        for y in range(height):
            for x in range(width):
                if pixdata[x, y] == (255, 255, 255, 255):
                    pixdata[x, y] = (255, 255, 255, 0)

    
    def pixels_comparison(self, figArray, figArray2):
        # in 'L', 255 is white
        white1 = np.count_nonzero(figArray)
        black1 = figArray.size - white1
        white2 = np.count_nonzero(figArray2)
        black2 = figArray2.size - white2
        difference = abs(black2 - black1)
        return difference
    
    def get_pixel_count(self, figArray):
        white = np.count_nonzero(figArray)
        black = figArray.size - white        
        return black    

    
    def find_nearest_neighbor(self, ans_array, array1, array2, array3):
        answer_compare = [self.pixels_comparison(x,array1) for x in ans_array]
        prob_pixels = self.pixels_comparison(array2,array3)
        nearest_list = [abs(prob_pixels - x) for x in answer_compare]
        nearestNeighbor = np.argmin(nearest_list)
        answer = nearestNeighbor + 1
        print(answer)
        return answer    
    
    def centerImageArray(self,figArray):
        figImage = Image.fromarray(figArray, "L")

        # mask
        threshold=128
        mask = figImage.point(lambda p: p < threshold and 255)

        # find edges
        edges = mask.filter(ImageFilter.FIND_EDGES)
        box = edges.getbbox()
        edges = edges.crop(box)

        # center in new image-figure
        tempImg = Image.new("L", figImage.size)

        width, height = edges.size
        fwidth, fheight = figImage.size

        tempImg.paste(edges, ((fwidth - width) // 2, (fheight - height) // 2))

        return np.array(tempImg)

    def MSE(self,arrayA, arrayB):
        return np.square(arrayA - arrayB).mean()

    def compare_images(self, arrayA, arrayB):
        # compute the mean squared error and structural similarity
        # index for the images
        m = self.MSE(arrayA, arrayB)
        
        return m
    
    def structural_similarity(self, array1, array2):
        ux = np.mean(array1)
        uy = np.mean(array2)
        uxx = ux*ux
        uyy = uy*uy
        
        xy = array1*array2
        uxy = np.mean(xy)
        
        xstd = np.std(array1)
        ystd = np.std(array2)
        xystd = np.std(xy)
        
        xv = uxx - ux * ux
        yv = uyy - uy * uy
        xyv = uxy - ux * uy
        
        C1 = (.8*255)**2
        C2 = (.9*255)**2
        
        ssim = (((2*ux*uy + C1)*(2*xyv + C2)/((uxx + uyy + C1)*(xv + yv + C2))))
        return ssim 

    
    def compare_pixels(self, list1, list2):
        
        if list1 != 0:
            m = (abs(list1 - list2)/list1)
            return m
        else:
            m = (abs(list1 - list2)/list2)
            return m

    def find_min(self, ans_array, array2):
        answer_compare = [self.compare_images(ans_array[str(x)],array2) for x in range(1,9)]
        answer_compare1 = [self.pixels_comparison(ans_array[str(x)],array2) for x in range(1,9)]
        min_array = np.argmin(answer_compare)
        min_array1 = np.argmin(answer_compare1)
        
        if min_array == min_array1:
            return min_array
        else:
            return min_array1
    

    def find_second_min_array(self, ans_array, array2):
        answer_compare = [self.compare_images(ans_array[str(x+ 1)],array2) for x in range(len(ans_array))]
        answer_compare1 = answer_compare
        answer_compare1.sort()
        length = len(answer_compare)
        second_smallest = answer_compare1[length - 2]

        for i in range(length):
            if answer_compare[i] == second_smallest:
                answer = i

        answer_comparepix = [self.pixels_comparison(ans_array[str(x+ 1)],array2) for x in range(len(ans_array))]
        answer_comparepix1 = answer_comparepix
        answer_comparepix1.sort()
        length1 = len(answer_comparepix)
        second_smallestpix = answer_comparepix1[length - 2]

        for i in range(length1):
            if answer_comparepix[i] == second_smallestpix:
                answerpix = i

                resultlist = [answer,answerpix]
                return resultlist 
    
    def find_second_min_list(self, list1):
        
        list1.sort()
        length = len(list1)
        second_smallest = list1[length - 2]

        for i in range(length):
            if list1[i] == second_smallest:
                answer = i
                
                return answer
    
    
          
    def sum_of_row(self, arrayA, arrayB, arrayC):
        
        A = self.get_pixel_count(arrayA)
        B = self.get_pixel_count(arrayB)
        C = self.get_pixel_count(arrayC)
        
        sumABC = A + B + C
        
        return sumABC
    
    def sum_of_pair(self, arrayA, arrayB):
        
        A = self.get_pixel_count(arrayA)
        B = self.get_pixel_count(arrayB)
        
        sumAB = A + B
        
        return sumAB
    
    def sum_of_ans(self, arrayG, arrayH, ans_array):
        
        G = self.get_pixel_count(arrayG)
        H = self.get_pixel_count(arrayH)
        
        sumOfAns = [(G + H + self.get_pixel_count(x)) for x in ans_array]
        
        return sumOfAns
    
    def diff_of_row(self, a, b, c):
        
        ab = self.pixels_comparison( a, b)
        bc = self.pixels_comparison( b, c)
        
        difference = abs(ab - bc)
        
        return difference 
    
    def diff_of_ans(self, g, h, ans_array):
        
        gh = self.pixels_comparison( g, h)
        
        diffOfAns = [abs(gh - self.pixels_comparison(h, ans_array[x])) for x in ans_array]
        
        return diffOfAns    
    
    def find_nearest_list(self, list1, list2,list3,list4, four):       

        rowListAD = [abs(list1[0] - x) for x in list4]
        rowListGH = abs(list1[0] - four)
        
        
        comboListAD = [abs(list1[1] - x) for x in list4]
        

        colListAB = [abs(list1[2] - x) for x in list2]
        colListAC = [abs(list1[2] - x) for x in list3]

        diagListAB = [abs(list1[3] - x) for x in list2]
        diagListAC = [abs(list1[3] - x) for x in list3]

        rowminAD = np.argmin(rowListAD)
        colminAB = np.argmin(colListAB)
        colminAC = np.argmin(colListAC)
        diagminAB = np.argmin(diagListAB)
        diagminAC = np.argmin(diagListAC)
        combolistmin = np.argmin(comboListAD)

        if diagminAB == 1 or diagminAB == 3:
            print('Cyclic pattern')
            return 1
        elif rowListAD == 0:
            if rowListGH == 0:
                print('pattern same ab2de2gh and bc2ef2hi')
                return 2
        elif combolistmin == 1:
            print('Combo or pattern same across rows')
            return 3
        else:
            return 4

    def nearest_answerHI(self, list1,list2):
        
        ansListHI = [abs(list1[0] - x) for x in list2]
        
        minAns = np.argmin(ansListHI)
        answer = minAns + 1
        print(answer)
        return answer
    
    def nearest_answerGI(self, list1,list2):
        
        ansListGI = [abs(list1[1] - x) for x in list2]
        
        minAns = np.argmin(ansListGI)
        
        answer = minAns + 1
        return answer
    
    def nearest_answerEI(self, list1,list2):
        
        ansListEI = [abs(list1[3] - x) for x in list2]
        
        minAns = np.argmin(ansListEI)
        
        answer = minAns + 1
        return answer    
    
    def nearest_answerFI(self, list1,list2):
        
        ansListFI = [abs(list1[2] - x) for x in list2]
        
        minAns = np.argmin(ansListFI)
        
        answer = minAns + 1
        return answer       


    def greater_than_list(self, ans_array, prob_array):

        if self.pixels_comparison(prob_array['A'],prob_array['B']) < self.pixels_comparison(prob_array['B'],prob_array['C']):
            i = 0
            max_list = []
            while i < len(ans_array):
                m = self.pixels_comparison(prob_array['H'],ans_array[str(i)])
                if m > self.pixels_comparison(prob_array['G'],prob_array['H']):
                    max_list.append(m)
                    i +=1 
                    return m     